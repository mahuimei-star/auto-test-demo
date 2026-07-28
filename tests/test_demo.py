import allure
import requests

BASE = "https://api.github.com"


@allure.title("Test get repository info")
@allure.feature("GitHub API")
def test_get_repos():
    r = requests.get(f"{BASE}/repos/maya085223-bot/auto-test-demo")
    assert r.status_code == 200
    assert r.json()["name"] == "auto-test-demo"


@allure.title("Test GitHub API root")
@allure.feature("GitHub API")
def test_get_root():
    r = requests.get(BASE)
    assert r.status_code == 200
