import requests


def test_get_request():
    r = requests.get("https://httpbin.org/get")
    assert r.status_code == 200


def test_post_request():
    r = requests.post("https://httpbin.org/post", json={"key": "value"})
    assert r.status_code == 200
    assert r.json()["json"]["key"] == "value"
