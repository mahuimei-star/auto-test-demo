import allure
from playwright.sync_api import sync_playwright


@allure.title("Test Baidu page title")
@allure.feature("UI Test")
def test_baidu_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.baidu.com")
        assert "百度" in page.title()
        browser.close()