from pydantic import BaseModel

from web_sdk.core.fields import APath
from web_sdk.enums import HTTPMethod
from web_sdk.sdks.rest import Client, ClientService, JsonResponse, Method, Service, Settings, get_res


# Response short data structure
class ShortData(BaseModel):
    pk: int = 1
    q: bool | None = None


# Response data structure
class Data(ShortData):
    nested: ShortData


# declare service for group of methods
class FooService(Service, path="data/{pk}/info"):
    get_data = Method[JsonResponse[Data]](method=HTTPMethod.GET)
    # declare method with return type and path (default method is GET)
    get_short_data = Method[JsonResponse[ShortData]](path="short")


# declare client service for group of real methods in client class
class FooClientService(ClientService):
    # declare method with certain signature pk is path part,
    # q is param (param type is default for GET method)
    @FooService.get_data
    def get_data(self, pk: APath[int], q: bool | None = None) -> JsonResponse[Data]: ...

    get_short_data = FooService.get_short_data.from_method(get_data)


# declare client class
class FooClient(Client):
    # set client services as annotation
    service: FooClientService


# init client settings
settings = Settings(protocol="http", host="127.0.0.1", api_path="api/v1", port=8000)

# init client instance
client = FooClient(settings=settings)

# make get_data request
data_response = client.service.get_data(pk=1, q=True)
# extract data from response
data = get_res(data_response)
# Data(pk=1, q=True, nested=ShortData(pk=1, q=True))

# make get_short_data request
short_data_response = client.service.get_short_data(pk=1, q=True)
# extract data from response
short_data = get_res(short_data_response)
# ShortData(pk=1, q=True)
