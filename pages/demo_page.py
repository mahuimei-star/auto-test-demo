from playwright.sync_api import Page


class DemoPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto("https://the-internet.herokuapp.com")

    def get_title(self) -> str:
        return self.page.title()

    def click_link(self, link_text: str):
        self.page.click(f"text={link_text}")

    def get_body_text(self) -> str:
        return self.page.text_content("body")