from web_sdk.enums import HTTPMethod
from web_sdk.sdks.rest import Method, Service

from . import schemas


class PaymentsService(
    Service,
    path="payments",
    description="Payments service",  # optional
):
    get = Method[schemas.GetPaymentResponse](
        path="{payment_id}",
        description="Get payment by id",  # optional
    )  # full path is "{settings.url}/payments/{payment_id}"

    make = Method[schemas.MakePaymentResponse](
        method=HTTPMethod.POST,
        path="make/{order_id}",
        description="Make payment for order",  # optional
    )  # full path is "{settings.url}/payments/make/{order_id}"


class OrdersService(
    Service,
    path="orders/{order_id}",
    description="Get order information by id",  # optional
):
    get = Method[schemas.GetOrderResponse](
        description="Get order information",  # optional
    )  # full path is "{settings.url}/orders/{order_id}"

    payments = Method[schemas.GetPaymentsResponse](
        path="payments",
        description="Get order payments",  # optional
    )  # full path is "{settings.url}/orders/{order_id}/payments"
