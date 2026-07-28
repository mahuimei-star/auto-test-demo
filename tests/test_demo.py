import requests


def test_get_request():
    r = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert r.status_code == 200


def test_post_request():
    r = requests.post("https://jsonplaceholder.typicode.com/posts", json={"title": "foo", "body": "bar"})
    assert r.status_code == 201
    assert r.json()["title"] == "foo"
