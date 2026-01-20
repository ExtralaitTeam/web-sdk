<img src="resources/brand.svg" width="100%" alt="Brand image" />

WebSDK is a library for quickly and easily creating SDKs for integration with third-party APIs.

## Supported backends

### Sync backends

#### Requests REST

Client and utils for declare the sync SDK based on [requests](https://github.com/psf/requests).
To get started, you can read the documentation for the [relevant section](pages/backends/rest/requests/index.md).

???- examples "Examples"
    === "Settings"
        ```py linenums="1" title="settings.py""
        --8<-- "home/sync/rest/settings.py"
        ```
    === "Schemas"
        ```py linenums="1" title="schemas.py""
        --8<-- "home/sync/rest/schemas.py"
        ```
    === "Methods"
        ```py linenums="1" title="methods.py""
        --8<-- "home/sync/rest/methods.py"
        ```
    === "Client"
        ```py linenums="1" title="client.py""
        --8<-- "home/sync/rest/client.py"
        ```
    === "Usage"
        ```py linenums="1" title="usage.py""
        --8<-- "home/sync/rest/usage.py"
        ```

#### Requests SOAP

In progress...

### Async backends

#### Httpx REST

Planned...

#### Httpx SOAP

Planned...
