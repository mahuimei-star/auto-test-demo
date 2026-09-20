import allure
import requests

BASE = "https://jsonplaceholder.typicode.com"


@allure.title("Test get a single post")
@allure.feature("JSONPlaceholder API")
def test_get_post():
    r = requests.get(f"{BASE}/posts/1")
    assert r.status_code == 200
    assert r.json()["id"] == 1


@allure.title("Test get post list")
@allure.feature("JSONPlaceholder API")
def test_get_posts():
    r = requests.get(f"{BASE}/posts")
    assert r.status_code == 200
    assert len(r.json()) == 100
