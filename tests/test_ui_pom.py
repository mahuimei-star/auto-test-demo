import allure
import pytest
from playwright.sync_api import sync_playwright
from pages.baidu_page import BaiduPage

search_data = [
    "pytest",
    "playwright",
    "allure",
]


@allure.title("Baidu page title test with data: {keyword}")
@allure.feature("UI Test - DDT")
@pytest.mark.parametrize("keyword", search_data)
def test_baidu_title(keyword):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        baidu = BaiduPage(page)
        baidu.navigate()
        assert keyword in baidu.get_title().lower()
        browser.close()