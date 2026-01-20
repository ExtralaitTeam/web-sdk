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
