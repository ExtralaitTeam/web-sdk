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
