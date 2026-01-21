<p align="center">
  <img src="docs/resources/brand.svg" width="100%" alt="Web SDK">
</p>
<p align="center">
    <em>WebSDK is a library for quickly and easily creating SDKs for integration with third-party APIs.</em>
</p>

<p align="center">

<a href="https://github.com/ExtralaitTeam/web-sdk/actions?query=event%3Apush+branch%3Amaster+workflow%3ACI" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/ExtralaitTeam/web-sdk/ci.yml?branch=master&logo=github&label=CI" alt="CI">
</a>
<a href="https://coverage-badge.samuelcolvin.workers.dev/redirect/ExtralaitTeam/web-sdk" target="_blank">
    <img src="https://coverage-badge.samuelcolvin.workers.dev/ExtralaitTeam/web-sdk.svg" alt="Coverage">
</a>
<a href="https://pypi.python.org/pypi/web-sdk" target="_blank">
    <img src="https://img.shields.io/pypi/v/web-sdk.svg" alt="pypi">
</a>
<a href="https://pepy.tech/project/web-sdk" target="_blank">
    <img src="https://static.pepy.tech/badge/web-sdk/month" alt="downloads">
</a>
<a href="https://github.com/ExtralaitTeam/web-sdk" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/web-sdk.svg" alt="versions">
</a>
<a href="https://github.com/ExtralaitTeam/web-sdk" target="_blank">
    <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/ExtralaitTeam/web-sdk/master/docs/badge/alfa.json" alt="Web SDK alfa">
</a>

</p>

[//]: # ([![llms.txt]&#40;https://img.shields.io/badge/llms.txt-green&#41;]&#40;https://docs.pydantic.dev/latest/llms.txt&#41;)
[//]: # ([![CondaForge]&#40;https://img.shields.io/conda/v/conda-forge/web-sdk.svg&#41;]&#40;https://anaconda.org/conda-forge/web-sdk&#41;)

# Installation

**REST installation**

Install using `pip install -U web-sdk[rest]` or `uv add web-sdk[rest]`

If you want to use `web_sdk.sdks.rest.XmlResponse`

Install using `pip install -U web-sdk[rest,xml]` or `uv add web-sdk[rest,xml]`

**SOAP installation**

Install using `pip install -U web-sdk[soap]` or `uv add web-sdk[soap]`

# Minimal example

**Server code**
```py
# docs/examples/home/minimal/server.py
```

**Client code**
```py
# docs/examples/home/minimal/client.py
```

# Features
- [x] Annotation like request parts mapper
- [x] All requests methods support
- [x] Pydantic validation output and input data
- [x] File sending
- [x] Custom extra and context data during request
- [x] Errors logging
- [x] Custom client settings
- [x] Custom and token auth
- [x] Test mode settings support
- [x] Requests REST support
  - [x] Service declaration base request configuring
  - [x] Method declaration base request configuring
  - [x] Method call base request configuring
  - [x] Request call base request configuring
  - [ ] Path part mapping without field annotation
- [x] Requests SOAP support
  - [x] Custom transport for file sending
  - [ ] Service declaration base request configuring
  - [ ] Method declaration base request configuring
  - [ ] Method call base request configuring
  - [ ] Request call base request configuring
- [ ] HTTPX REST support
- [ ] HTTPX SOAP support
- [ ] MkDocs documentation

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
