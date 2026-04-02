from faker.generator import random

from locators.alert_frame_windows_locators import AlertsPageLocators, BrowserWindowsPageLocators, FramesPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()
    def check_opened_new_tab(self):
        self.click_and_switch_to_new_window(self.locators.NEW_TAB_BUTTON)
        return self.find_is_present(self.locators.TEXT_NEW_TAB).text

    def check_opened_new_window(self):
        self.click_and_switch_to_new_window(self.locators.NEW_WINDOW_BUTTON)
        return self.find_is_present(self.locators.TEXT_NEW_WINDOW).text
    
class AlertsPage(BasePage):
    locators = AlertsPageLocators()
    def check_see_alert(self):
        return self.click_and_handle_alert(self.locators.SEE_ALERT_BUTTON)

    def check_see_alert_after_5_sec(self):
        return self.click_and_handle_alert(
            self.locators.APPEAR_ALERT_AFTER_5_SEC_BUTTON,
            timeout=10
        )

    
    def check_confirm_box_alert(self):
        action = random.choice(["accept", "dismiss"])
        self.click_and_handle_alert(
            self.locators.CONFIRM_BOX_ALERT_BUTTON,
            action=action
        )
        return self.find_is_visible(self.locators.CONFIRM_RESULT).text

    
    def check_prompt_box_alert(self, input_text):
        self.click_and_handle_alert(
            self.locators.PROMPT_BOX_ALERT_BUTTON,
            input_text=input_text
        )
        return self.find_is_visible(self.locators.PROMPT_RESULT).text

class FramesPage(BasePage):
    locators = FramesPageLocators()
    def check_frames(self, frame_number):
        frames = {
            "frame_1": self.locators.FRAME_1,
            "frame_2": self.locators.FRAME_2,
        }
    
        if frame_number not in frames:
            raise ValueError(f"Unknown frame: {frame_number}")
    
        return self.get_frame_data(frames[frame_number], self.locators.TEXT_FRAME)
