from playwright.sync_api import Page


class BaiduPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto("https://www.baidu.com")

    def get_title(self) -> str:
        return self.page.title()