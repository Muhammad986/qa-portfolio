import allure
from faker.generator import random

from locators.alert_frame_windows_locators import AlertsPageLocators, BrowserWindowsPageLocators, FramesPageLocators, ModalDialogsPageLocators, NestedFramesPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    @allure.step('Check opened new tab')
    def check_opened_new_tab(self):
        self.click_and_switch_to_new_window(self.locators.NEW_TAB_BUTTON)
        return self.find_is_present(self.locators.TEXT_NEW_TAB).text

    @allure.step('Check opened new window')
    def check_opened_new_window(self):
        self.click_and_switch_to_new_window(self.locators.NEW_WINDOW_BUTTON)
        return self.find_is_present(self.locators.TEXT_NEW_WINDOW).text
    
class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    @allure.step('Check see alert')
    def check_see_alert(self):
        return self.click_and_handle_alert(self.locators.SEE_ALERT_BUTTON)

    @allure.step('Check alert after 5 seconds')
    def check_see_alert_after_5_sec(self):
        return self.click_and_handle_alert(
            self.locators.APPEAR_ALERT_AFTER_5_SEC_BUTTON,
            timeout=10
        )

    @allure.step('Check confirm box alert')
    def check_confirm_box_alert(self):
        action = random.choice(["accept", "dismiss"])
        self.click_and_handle_alert(
            self.locators.CONFIRM_BOX_ALERT_BUTTON,
            action=action
        )
        return self.find_is_visible(self.locators.CONFIRM_RESULT).text

    @allure.step('Check prompt box alert')
    def check_prompt_box_alert(self, input_text):
        self.click_and_handle_alert(
            self.locators.PROMPT_BOX_ALERT_BUTTON,
            input_text=input_text
        )
        return self.find_is_visible(self.locators.PROMPT_RESULT).text

class FramesPage(BasePage):
    locators = FramesPageLocators()
    @allure.step('Check frames')
    def check_frames(self, frame_number):
        frames = {
            "frame_1": self.locators.FRAME_1,
            "frame_2": self.locators.FRAME_2,
        }
    
        if frame_number not in frames:
            raise ValueError(f"Unknown frame: {frame_number}")
    
        return self.get_frame_data(frames[frame_number], self.locators.TEXT_FRAME)
    
class NestedFramesPage(BasePage):
    locators = NestedFramesPageLocators() 

    @allure.step('Check nested frames')
    def check_nested_frames(self):
        parent_frame = self.get_frame_data(
            self.locators.PARENT_FRAME, 
            self.locators.TEXT_PARENT_FRAME, 
            switch_back=None
            )
        child_frame = self.get_frame_data(
            self.locators.CHILD_FRAME,
            self.locators.TEXT_CHILD_FRAME,
            switch_back="default"
            )
        return parent_frame, child_frame

class ModalDialogsPage(BasePage):
    locators = ModalDialogsPageLocators()

    @allure.step('Check small modal dialog')
    def check_small_modal_dialog(self):
        self.find_is_clickable(self.locators.SMALL_MODAL_BUTTON).click()
        title = self.find_is_present(self.locators.TITLE_MODAL).text
        text_body = self.find_is_present(self.locators.TEXT_MODAL).text
        self.find_is_clickable(self.locators.CLOSE_SMALL_MODAL_BUTTON).click()
        return [title, len(text_body)]
    
    @allure.step('Check large modal dialog')
    def check_large_modal_dialog(self):
        self.find_is_clickable(self.locators.LARGE_MODAL_BUTTON).click()
        title = self.find_is_present(self.locators.TITLE_MODAL).text
        text_body = self.find_is_present(self.locators.TEXT_MODAL).text
        self.find_is_clickable(self.locators.CLOSE_LARGE_MODAL_BUTTON).click()
        return [title, len(text_body)]