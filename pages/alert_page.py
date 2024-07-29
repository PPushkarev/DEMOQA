from locators.alert_page_locators import BrowserWindowsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage (BasePage):
    locators = BrowserWindowsPageLocators()

    def check_open_new_tab(self):
        self.element_is_visable(self.locators.NEW_TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title

    def check_open_new_window(self):
        self.element_i_visable(self.locators.NEW_WINDOW_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title

