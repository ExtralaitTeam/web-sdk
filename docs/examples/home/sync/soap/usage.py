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
