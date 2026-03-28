import random
import re
import time
from typing import Iterable, Set

from selenium.webdriver.common.by import By

from locators.elements_page_locators import CheckBoxPageLocators, RadioButtonPageLocators, TextBoxPageLocators, WebTablePageLocators
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

                
                count -= 1
            else:
                break
    def normalize_text_items(self, items: Iterable[str]) -> list[str]:
        norm = lambda s: re.sub(
            r"[^a-z0-9а-яё]+", "",
            re.sub(r"\.[a-z0-9]+$", "", s.strip().lower())
        )
        normalize = [norm(s) for s in items]
        return sorted(normalize)
    
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
    
class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    def click_on_the_radio_button(self, radio_button):
        choices = {
            'yes': self.locators.YES_RADIO,
            'impressive': self.locators.IMPRESSIVE_RADIO,
            'no': self.locators.NO_RADIO
        }
        if radio_button in choices:
            self.find_is_visible(choices[radio_button]).click()
        else:
            raise ValueError(f"Invalid radio button choice: {radio_button}")
        

    
    def get_output_result(self):
        return self.find_is_visible(self.locators.OUTPUT_RESULT).text
    

class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    def add_new_person(self) -> list[str]:
        count = 1
        while count != 0:
            person_info = next(generated_person())
            first_name = person_info.first_name
            last_name = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department

            self.find_is_visible(self.locators.ADD_BUTTON).click()
            self.find_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(first_name)
            self.find_is_visible(self.locators.LAST_NAME_INPUT).send_keys(last_name)
            self.find_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.find_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.find_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.find_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.find_is_visible(self.locators.SUBMIT_BUTTON).click()

            
            count -= 1

            return [first_name, last_name, str(age), email, str(salary), department]
        
    def check_added_person(self):
        person_list = self.find_are_present(self.locators.FULL_PEOPLE_LIST)
        data = [item.text.split(maxsplit=5) for item in person_list]
        return data
    
    def search_some_person(self, key):
        self.find_is_visible(self.locators.SEARCH_INPUT).send_keys(key)

    def check_search_person(self):
        delete_buttons = self.driver.find_elements(*self.locators.DELETE_BUTTON)
        if not delete_buttons:
            return ""
        row = delete_buttons[0].find_element(*self.locators.ROW_PARENT)
        return row.text
    
    def update_person_info(self):
        person_info = next(generated_person())
        updatable_fields = {
            "first_name": (self.locators.FIRST_NAME_INPUT, person_info.first_name),
            "email": (self.locators.EMAIL_INPUT, person_info.email),
            "age": (self.locators.AGE_INPUT, str(person_info.age)),
            "salary": (self.locators.SALARY_INPUT, str(person_info.salary)),
        }
        field_name = random.choice(list(updatable_fields.keys()))
        field_locator, new_value = updatable_fields[field_name]

        self.find_is_visible(self.locators.UPDATE_BUTTON).click()
        input_field = self.find_is_visible(field_locator)
        input_field.clear()
        input_field.send_keys(new_value)
        self.find_is_visible(self.locators.SUBMIT_BUTTON).click()

        return field_name, new_value
    

    def delete_person(self):
        delete_buttons = self.driver.find_elements(*self.locators.DELETE_BUTTON)
        if delete_buttons:
            delete_buttons[0].click()

    def select_up_to_some_rows(self):
        count = [10, 20, 30, 40, 50]
        data = []
        for c in count:
            count_row_button = self.find_is_visible(self.locators.COUNT_ROW_LIST)
            self.go_to_element(count_row_button)
            count_row_button.click()
            self.find_is_visible((By.CSS_SELECTOR, f'option[value="{c}"]')).click()
            data.append(self.check_count_rows())
        return data

    
    def check_count_rows(self):
        table_rows = self.find_is_visible(self.locators.COUNT_ACTIVE_ROW)
        return int(table_rows.get_attribute('value'))

            
        