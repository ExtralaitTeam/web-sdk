<p align="center">
  <img src="docs/resources/brand.svg" width="100%" alt="Web SDK">
</p>
<p align="center">
    <em>WebSDK is a library for quickly and easily creating SDKs for integration with third-party APIs.</em>
</p>

# Installation

**REST installation**

Install using `pip install -U web-sdk[rest]` or `uv add web-sdk[rest]`

If you want to use `web_sdk.sdks.rest.XmlResponse`
Install using `pip install -U web-sdk[rest,xml]` or `uv add web-sdk[rest,xml]`

**SOAP installation**

Install using `pip install -U web-sdk[soap]` or `uv add web-sdk[soap]`

# Supported backends


## Sync backends


### Requests REST


Client and utils for declare the sync SDK based on [requests](https://github.com/psf/requests).

#### Declare custom or use default settings
```py
# docs/examples/home/sync/rest/settings.py
```

#### Create responses schemas
```py
# docs/examples/home/sync/rest/schemas.py
```

#### Declare services with methods for using in client
```py
# docs/examples/home/sync/rest/methods.py
```

#### Declare client and client services
```py
# docs/examples/home/sync/rest/client.py
```

#### Usage example
```py
# docs/examples/home/sync/rest/usage.py
```

### Requests SOAP

Client and utils for declare the sync SDK based on [requests](https://github.com/psf/requests), and [zeep](https://github.com/mvantellingen/python-zeep).


#### Declare custom or use default settings
```py
# docs/examples/home/sync/soap/settings.py
```

#### Create responses schemas
```py
# docs/examples/home/sync/soap/schemas.py
```

#### Declare services with methods for using in client
```py
# docs/examples/home/sync/soap/methods.py
```

#### Declare client and client services
```py
# docs/examples/home/sync/soap/client.py
```

#### Usage example
```py
# docs/examples/home/sync/soap/usage.py
```

## Async backends
Planned...


### Httpx REST


Planned...


### Httpx SOAP


Planned...
