import requests

BASE = "https://api.github.com"


def test_get_repos():
    r = requests.get(f"{BASE}/repos/maya085223-bot/auto-test-demo")
    assert r.status_code == 200
    assert r.json()["name"] == "auto-test-demo"


def test_get_root():
    r = requests.get(BASE)
    assert r.status_code == 200
