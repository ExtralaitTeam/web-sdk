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
