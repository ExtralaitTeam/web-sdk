from pydantic_settings import SettingsConfigDict

from web_sdk.core.bases import BaseSDKSettings

# Here you can make next instead of RestRequestsSettings import
# from web_sdk.backends.rest.requests import Settings


class FooSettings(BaseSDKSettings):
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
