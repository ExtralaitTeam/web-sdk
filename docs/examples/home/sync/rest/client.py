from decimal import Decimal
from typing import Annotated

from typing_extensions import Unpack

from web_sdk.core.backends.requests.rest.kwargs import RestRequestsKwargsWithSettings
from web_sdk.core.fields import APath, ASetting, Body, Param, Path
from web_sdk.sdks.rest import Client, ClientService

from . import schemas
from .methods import OrdersService, PaymentsService
from .settings import FooSettings


class _BaseFooClient(Client, base=True):
    """Here you can customize the client logic to suit your needs."""

    __default_settings_class__ = FooSettings


class FooClientService(ClientService[_BaseFooClient], client=_BaseFooClient):
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
        immediately: bool | None = Param(None),
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


class FooClient(_BaseFooClient):
    payments: PaymentsClientService
    orders: PaymentsClientService
