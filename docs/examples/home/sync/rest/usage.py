from web_sdk.core.bases.rest.schemas import get_res
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
response = client.payments.get(
    payment_id=1,
    timeout=1,
    raise_exceptions=False,
)

result_or_none = get_res(response, required=False)
result = get_res(response)
