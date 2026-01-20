[//]: # (DO NOT CHANGE THIS FILE MANUALLY. Use "make embed-readme" after changing template file)
<p align="center">
  <img src="docs/resources/brand.svg" width="100%" alt="Web SDK">
</p>
<p align="center">
    <em>WebSDK is a library for quickly and easily creating SDKs for integration with third-party APIs.</em>
</p>

## Supported backends


### Sync backends


#### Requests REST


Client and utils for declare the sync SDK based on [requests](https://github.com/psf/requests).

##### Declare custom or use default settings
```py
# docs/examples/home/sync/rest/settings.py

from pydantic_settings import SettingsConfigDict

from web_sdk.sdks.rest import Settings


class FooSettings(Settings):
    protocol: str = "https"
    """API protocol"""
    host: str = "example.com"
    """API host"""
    port: int | None = 8000
    """API port"""
    api_path: str = "/api/v1"
    """API path"""

    model_config = SettingsConfigDict(
        env_prefix="FOO_CLIENT_",
    )

```

##### Create responses schemas
```py
# docs/examples/home/sync/rest/schemas.py

from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel

from web_sdk.sdks.rest import JsonResponse


class PaymentShortInfoDTO(BaseModel):
    id: str
    is_success: bool


class PaymentInfoDTO(PaymentShortInfoDTO):
    order_id: str
    payment_date: datetime
    payment_amount: Decimal


class OrderShortInfoDTO(BaseModel):
    id: str
    reference: str


class OrderInfoDTO(OrderShortInfoDTO):
    class _TargetDTO(BaseModel):
        id: str
        type: str
        price: Decimal

    # it is working with nested model
    target: _TargetDTO


GetPaymentResponse = JsonResponse[PaymentInfoDTO]
# it is working with list data
GetPaymentsResponse = JsonResponse[list[PaymentInfoDTO]]
MakePaymentResponse = JsonResponse[PaymentShortInfoDTO]
GetOrderResponse = JsonResponse[OrderInfoDTO]

```

##### Declare services with methods for using in client
```py
# docs/examples/home/sync/rest/methods.py

from web_sdk.enums import HTTPMethod
from web_sdk.sdks.rest import Method, Service

from . import schemas


class PaymentsService(
    Service,
    path="payments",
    description="Payments service",
):
    get = Method[schemas.GetPaymentResponse](
        path="{payment_id}",
        description="Get payment by id",
    )  # full path is "{settings.url}/payments/{payment_id}"

    make = Method[schemas.MakePaymentResponse](
        method=HTTPMethod.POST,
        path="make/{order_id}",
        description="Make payment for order",
    )  # full path is "{settings.url}/payments/make/{order_id}"


class OrdersService(
    Service,
    path="orders/{order_id}",
    description="Get order information by id",
):
    get = Method[schemas.GetOrderResponse](
        description="Get order information",
    )  # full path is "{settings.url}/orders/{order_id}"

    payments = Method[schemas.GetPaymentsResponse](
        path="payments",
        description="Get order payments",
    )  # full path is "{settings.url}/orders/{order_id}/payments"

```

##### Declare client and client services
```py
# docs/examples/home/sync/rest/client.py

from decimal import Decimal
from typing import Annotated

from typing_extensions import Unpack

from web_sdk.core.backends.requests.rest.kwargs import RestRequestsKwargsWithSettings
from web_sdk.core.fields import APath, ASetting, Body, Param, Path
from web_sdk.sdks.rest import Client, ClientService

from . import schemas
from .methods import OrdersService, PaymentsService
from .settings import FooSettings


class BaseFooClient(Client, base=True):
    """Here you can customize the client logic to suit your needs."""

    __default_settings_class__ = FooSettings


class FooClientService(ClientService[BaseFooClient], client=BaseFooClient):
    """This class need for isolate subclasses registering in user class."""


class PaymentsClientService(FooClientService):
    @PaymentsService.get
    def get(
        self,
        # ALike aliases (shortcut for Annotated[T, Field])
        payment_id: APath[int],
        # Unpack with TypedDict
        **kwargs: Unpack[RestRequestsKwargsWithSettings],
    ) -> schemas.GetPaymentResponse: ...

    @PaymentsService.make(timeout=5)
    def make(
        self,
        # Annotated[T, Field] like annotations
        order_id: Annotated[str, Path],
        # Other variant with Field call
        amount: Annotated[Decimal, Body(ge=Decimal("0"))],
        # Field as default value. You can also use a field without
        # specifying a default value, then the field will be
        # required (arg: bool = Param) or (arg: bool = Param()).
        immediately: bool | None = Param(None),  # type: ignore
        # Using settings to change Client.make_request behavior
        raise_exception: ASetting[bool | None] = None,
    ) -> schemas.MakePaymentResponse: ...


class OrdersClientService(FooClientService):
    @OrdersService.get
    def get(self, order_id: APath[int]) -> schemas.GetOrderResponse: ...

    @OrdersService.get
    def payments(
        self,
        order_id: APath[int],
        # For GET, DELETE, OPTION, HEAD methods default field is Param,
        # for POST, PATCH, PUT methods default field id Body
        success_only: bool = False,
    ) -> schemas.GetPaymentsResponse: ...


class FooClient(BaseFooClient):
    payments: PaymentsClientService
    orders: PaymentsClientService

```

##### Usage example
```py
# docs/examples/home/sync/rest/usage.py

from web_sdk.core.utils import make_client_factory
from web_sdk.sdks.rest import get_res

from .client import FooClient
from .settings import FooSettings

# You can just create client instance
# client = FooClient()

# But I recommend creating a client factory to cache instances
# based on the settings and logger hashes to avoid creating duplicate instances
client_factory = make_client_factory(FooClient, FooSettings)


# Create client
client = client_factory()

# Method response or error response if you use raise_exceptions=False
# or None if you use skip_for_tests
response = client.payments.get(
    payment_id=1,
    timeout=1,
    raise_exceptions=False,
)

result_or_none = get_res(response, required=False)
result = get_res(response)

```

#### Requests SOAP

Client and utils for declare the sync SDK based on [requests](https://github.com/psf/requests), and [zeep](https://github.com/mvantellingen/python-zeep).


##### Declare custom or use default settings
```py
# docs/examples/home/sync/soap/settings.py

from pydantic_settings import SettingsConfigDict

from web_sdk.sdks.soap import Settings


class FooSettings(Settings):
    protocol: str = "https"
    """API protocol"""
    host: str = "example.com"
    """API host"""
    port: int | None = 8000
    """API port"""
    api_path: str = "/api/v1"
    """API path"""
    service_name: str | None = "service"
    """The name of wsdl service."""
    port_name: str | None = "port"
    """The name of wsdl port."""

    model_config = SettingsConfigDict(
        env_prefix="FOO_CLIENT_",
    )

```

##### Create responses schemas
```py
# docs/examples/home/sync/soap/schemas.py

from datetime import datetime
from decimal import Decimal
from typing import Generic

from pydantic import BaseModel

from web_sdk.contrib.pydantic.model import PydanticModel
from web_sdk.core.bases.soap import SoapFile
from web_sdk.sdks.soap import SoapResponse
from web_sdk.types import TData


class PaymentShortInfoDTO(PydanticModel):
    id: str
    is_success: bool


class PaymentInfoDTO(PydanticModel):
    order_id: str
    payment_date: datetime
    payment_amount: Decimal
    document: SoapFile


class PaymentsInfosDTO(PydanticModel):
    payments: list[PaymentInfoDTO]


class OrderShortInfoDTO(PydanticModel):
    id: str
    reference: str


class OrderInfoDTO(PydanticModel):
    class _TargetDTO(BaseModel):
        id: str
        type: str
        price: Decimal

    # it is working with nested model
    target: _TargetDTO


class FooResponse(SoapResponse, Generic[TData]):
    success: bool
    data: TData


GetPaymentResponse = FooResponse[PaymentInfoDTO]
GetPaymentsResponse = FooResponse[list[PaymentInfoDTO]]
MakePaymentResponse = FooResponse[PaymentShortInfoDTO]
GetOrderResponse = FooResponse[OrderInfoDTO]

```

##### Declare services with methods for using in client
```py
# docs/examples/home/sync/soap/methods.py

from web_sdk.sdks.soap import Method, Service

from . import schemas


class PaymentsService(
    Service,
    path="Payments",
    description="Payments service",
):
    get = Method[schemas.GetPaymentResponse](
        path="getPayment",
        description="Get payment by id",
    )  # method path is "Payments.getPayment"

    make = Method[schemas.MakePaymentResponse](
        path="makePayment",
        description="Make payment for order",
    )  # method path is "Payments.makePayment"


class OrdersService(
    Service,
    description="Get order information by id",
):
    get = Method[schemas.GetOrderResponse](
        description="Get order information",
    )  # method path is "get"

    payments = Method[schemas.GetPaymentsResponse](
        path="paymentsWithPath",
        description="Get order payments",
    )  # method path is "paymentsWithPath"

```

##### Declare client and client services
```py
# docs/examples/home/sync/soap/client.py

from decimal import Decimal
from typing import Annotated

from typing_extensions import Unpack

from web_sdk.core.backends.requests.soap.kwargs import SoapRequestsKwargsWithSettings
from web_sdk.core.fields import AFile, ASetting, Body
from web_sdk.sdks.soap import Client, ClientService, SoapFile

from . import schemas
from .methods import OrdersService, PaymentsService
from .settings import FooSettings


class BaseFooClient(Client, base=True):
    """Here you can customize the client logic to suit your needs."""

    __default_settings_class__ = FooSettings


class FooClientService(ClientService[BaseFooClient], client=BaseFooClient):
    """This class need for isolate subclasses registering in user class."""


# For soap client Body is base field type
class PaymentsClientService(FooClientService):
    @PaymentsService.get
    def get(
        self,
        # ALike aliases (shortcut for Annotated[T, Field])
        payment_id: int,
        # Unpack with TypedDict
        **kwargs: Unpack[SoapRequestsKwargsWithSettings],
    ) -> schemas.GetPaymentResponse: ...

    @PaymentsService.make
    def make(
        self,
        # Annotated[T, Field] like annotations
        order_id: Annotated[str, Body],
        # Other variant with Field call
        amount: Annotated[Decimal, Body(ge=Decimal("0"))],
        # Field as default value. You can also use a field without
        # specifying a default value, then the field will be
        # required (arg: bool = Body) or (arg: bool = Body()).
        immediately: bool | None = Body(None),  # type: ignore
        # Send single file with request
        payment_file: AFile[SoapFile | None] = None,
        # Send multiple files with request
        other_files: AFile[list[SoapFile] | None] = None,
        # Using settings to change Client.make_request behavior
        raise_exception: ASetting[bool | None] = None,
    ) -> schemas.MakePaymentResponse: ...


class OrdersClientService(FooClientService):
    @OrdersService.get
    def get(self, order_id: int) -> schemas.GetOrderResponse: ...

    @OrdersService.get
    def payments(
        self,
        order_id: int,
        success_only: bool = False,
    ) -> schemas.GetPaymentsResponse: ...


class FooClient(BaseFooClient):
    payments: PaymentsClientService
    orders: PaymentsClientService

```

##### Usage example
```py
# docs/examples/home/sync/soap/usage.py

from decimal import Decimal

from web_sdk.core.bases.soap import SoapFile
from web_sdk.core.utils import make_client_factory

from .client import FooClient
from .settings import FooSettings

# You can just create client instance
# client = FooClient()

# But I recommend creating a client factory to cache instances
# based on the settings and logger hashes to avoid creating duplicate instances
client_factory = make_client_factory(FooClient, FooSettings)


# Create client
client = client_factory()

# Method response or error response if you use raise_exceptions=False
# or None if you use skip_for_tests
response = client.payments.make(
    order_id="123",
    amount=Decimal("100"),
    payment_file=SoapFile(
        filename="payment.txt",
        content_type="text/plain",
        content=b"content",
    ),
    raise_exception=False,
)

```

### Async backends
Planned...


#### Httpx REST


Planned...


#### Httpx SOAP


Planned...
