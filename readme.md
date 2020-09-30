Prototype of a python client for Camunda BPM

Features:

- Simple and easy to use API
- Support for both synchronous/asynchronous requests via `HTTPX`
- Type hints for 100% of a codebase
- No dictionaries — all requests and responses are data transfer objects built with `Pydantic`

State of a project: prototype. Project structure and base API is defined, but there
is currently only one endpoint implemented, see examples directory.

For working Camunda BPM client, please see
[pycamunda](https://pycamunda.readthedocs.io/en/latest/index.html)
