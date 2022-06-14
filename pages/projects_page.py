from playwright.sync_api import Page

from utils.playwright_utils import PlaywrightUtils


class ProjectPage:
    def __init__(self, page: Page):
        self.page = page
        self.playwright_utils = PlaywrightUtils(page)

    # private locators

    # getters
