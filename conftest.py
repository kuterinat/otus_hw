import pytest
import requests


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://ya.ru")
    parser.addoption("--status_code", action="store", default=200)


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")


class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, path="/", params=None, headers=None):
        url = f"{self.base_url}{path}"
        return requests.get(url=url, params=params, headers=headers)

    def post(self, path='/', params=None, data=None, headers=None):
        url = f"{self.base_url}{path}"
        return requests.post(url=url, params=params, data=data, headers=headers)

    def delete(self, path='/', params=None, headers=None):
        url = f"{self.base_url}{path}"
        return requests.delete(url=url, params=params, headers=headers)


@pytest.fixture
def dog_api():
    return ApiClient(base_url='https://dog.ceo/api/')


@pytest.fixture
def brewery_api():
    return ApiClient(base_url='https://api.openbrewerydb.org/breweries/')


@pytest.fixture
def typicode_api():
    return ApiClient(base_url='https://jsonplaceholder.typicode.com/')


@pytest.fixture
def all_breweries(brewery_api):
    resp = brewery_api.get('', params={'per_page': 50})
    return resp.json()
