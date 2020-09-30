_CAMUNDA_URL = "http://localhost:8080/engine-rest/"


def init(camunda_rest_api_url: str):
    global _CAMUNDA_URL
    _CAMUNDA_URL = camunda_rest_api_url


def get_api_url() -> str:
    return _CAMUNDA_URL
