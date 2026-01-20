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
