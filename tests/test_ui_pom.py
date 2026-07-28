import allure
import pytest
from playwright.sync_api import sync_playwright
from pages.demo_page import DemoPage


@allure.title("Test the-internet page loads")
@allure.feature("UI Test")
def test_page_loads():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        demo = DemoPage(page)
        demo.navigate()
        assert "The Internet" in demo.get_title()
        browser.close()


@allure.title("Test click link on the-internet")
@allure.feature("UI Test - POM + DDT")
@pytest.mark.parametrize("link", ["A/B Testing", "Checkboxes", "Dropdown"])
def test_click_link(link):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        demo = DemoPage(page)
        demo.navigate()
        demo.click_link(link)
        assert link in demo.get_body_text()
        browser.close()