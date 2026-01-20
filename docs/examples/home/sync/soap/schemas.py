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
