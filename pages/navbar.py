from playwright.sync_api import Page

from utils.playwright_utils import PlaywrightUtils


class Navbar:
    def __init__(self, page: Page):
        self.page = page
        self.playwright_utils = PlaywrightUtils(page)

    # private locators
    __LOGIN_SIGNUP_XPATH = "//a[contains(@href, 'login')]"

    # getters

    # clicks

    # booleans
    def is_login_sign_up_button_available(self) -> bool:
        return self.page.locator(self.__LOGIN_SIGNUP_XPATH).is_visible()