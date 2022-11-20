import requests


def test_ya_ru(url, status_code):
    resp = requests.get(url=url)
    assert str(resp.status_code) == status_code
