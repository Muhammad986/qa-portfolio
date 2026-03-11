import random
import re
from typing import Iterable, Set

from locators.elements_page_locators import CheckBoxPageLocators, TextBoxPageLocators
from pages.base_page import BasePage
from generator.generator import generated_person


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address

        self.find_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.find_is_visible(self.locators.EMAIL).send_keys(email)
        self.find_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.find_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(
            permanent_address
        )
        self.find_is_visible(self.locators.SUBMIT_BUTTON).click()

        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.find_is_present(self.locators.CREATED_FULL_NAME).text.split(
            ":"
        )[1]
        email = self.find_is_present(self.locators.CREATED_EMAIL).text.split(":")[1]
        current_address = self.find_is_present(
            self.locators.CREATED_CURRENT_ADDRESS
        ).text.split(":")[1]
        permanent_address = self.find_is_present(
            self.locators.CREATED_PERMANENT_ADDRESS
        ).text.split(":")[1]

        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        while True:
            closed_switchers = self.driver.find_elements(*self.locators.SWITCHER_CLOSE)
            if not closed_switchers:
                break
            closed_switchers[0].click()

    def click_random_checkbox(self):
        item_list = self.driver.find_elements(*self.locators.CHECKBOX_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(0, len(item_list) - 1)]
            if count > 0:
                self.go_to_element(item)
                self.driver.execute_script("arguments[0].click();", item)

                #print(item.text)
                count -= 1
            else:
                break
    def normalize_text_items(self, items: Iterable[str]) -> list[str]:
        norm = lambda s: re.sub(
            r"[^a-z0-9а-яё]+", "",
            re.sub(r"\.[a-z0-9]+$", "", s.strip().lower())
        )
        normalaze = [norm(s) for s in items]
        return sorted(normalaze)
    
    def get_checked_checkboxes(self):
        checked_list = self.find_are_present(self.locators.CHECKED_ITEMS)
        checked_items = []
        for box in checked_list:
            title_item = box.find_element(*self.locators.TITLE_ITEM)
            checked_items.append(title_item.text)

        checked_items = self.normalize_text_items(checked_items)
        return checked_items
        
    def get_output_result(self):
        result_list = self.find_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        data = self.normalize_text_items(data)
        return data
        