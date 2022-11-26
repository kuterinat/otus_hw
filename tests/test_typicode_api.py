import pytest
from random import choice

SUCC_STATUS_CODE = 200
CRT_STATUS_CODE = 201
ERR_STATUS_CODE = 404
ERR_MSG = ""
RESOURCES_NUMBER = [('posts', 100), ('comments', 500), ('albums', 100), ('photos', 5000), ('todos', 200), ('users', 10)]


def get_rand_resource_id(typicode_api, resource):
    resp = typicode_api.get(resource)
    return choice(resp.json())['id']


@pytest.mark.parametrize("resource, number", RESOURCES_NUMBER)
def test_get_list_of_resource(typicode_api, resource, number):
    resp = typicode_api.get(resource)
    assert resp.status_code == SUCC_STATUS_CODE, f"Wrong response code: {resp.status_code}"
    resources_items = resp.json()
    assert len(resources_items) == number, f"Wrong number of {resource}: {len(resources_items)}"


@pytest.mark.parametrize("resource", [r[0] for r in RESOURCES_NUMBER])
def test_get_resource_by_id(typicode_api, resource):
    resource_id = get_rand_resource_id(typicode_api, resource)
    resp = typicode_api.get(f"{resource}/{resource_id}")
    assert resp.status_code == SUCC_STATUS_CODE, f"Wrong response code: {resp.status_code}"
    resource_data = resp.json()
    assert 'id' in resource_data and resource_data['id'] == resource_id


@pytest.mark.parametrize("resource", ['posts', 'albums', 'todos'])
def test_get_user_resources(typicode_api, resource):
    user_id = get_rand_resource_id(typicode_api, 'users')
    resp = typicode_api.get(f"users/{user_id}/{resource}")
    assert resp.status_code == SUCC_STATUS_CODE, f"Wrong response code: {resp.status_code}"
    assert all(r['userId'] == user_id for r in resp.json())


def test_add_new_post(typicode_api):
    post_data = {'userId': str(get_rand_resource_id(typicode_api, 'users')), 'title': 'some title', 'body': 'some body'}
    resp = typicode_api.post(f"posts", data=post_data)
    assert resp.status_code == CRT_STATUS_CODE, f"Wrong response code: {resp.status_code}"
    created_post = resp.json()
    new_post_id = created_post.pop('id')
    assert created_post == post_data, f"Created post differs from post data"


def test_delete_post(typicode_api):
    post_id = get_rand_resource_id(typicode_api, 'posts')
    resp = typicode_api.delete(f"posts/{post_id}")
    assert resp.status_code == SUCC_STATUS_CODE, f"Wrong response code: {resp.status_code}"
    assert resp.json() == {}


@pytest.mark.parametrize("resource", [r[0] for r in RESOURCES_NUMBER])
def test_get_resource_by_id_incorrect(typicode_api, resource):
    resp = typicode_api.get(resource)
    assert resp.status_code == SUCC_STATUS_CODE, f"Wrong response code: {resp.status_code}"
    resource_ids = [r['id'] for r in resp.json()]
    resource_id = max(resource_ids) + 1
    resp = typicode_api.get(f"{resource}/{resource_id}")
    assert resp.status_code == ERR_STATUS_CODE, f"Wrong response code: {resp.status_code}"
