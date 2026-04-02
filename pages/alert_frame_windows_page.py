from locators.alert_frame_windows_locators import BrowserWindowsPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage

class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()
    def check_opened_new_tab(self):
        self.click_and_switch_to_new_window(self.locators.NEW_TAB_BUTTON)
        return self.find_is_present(self.locators.TEXT_NEW_TAB).text

    def check_opened_new_window(self):
        self.click_and_switch_to_new_window(self.locators.NEW_WINDOW_BUTTON)
        return self.find_is_present(self.locators.TEXT_NEW_WINDOW).text
    