#import base64, uuid
import os
import random
import re
import requests
import time
from typing import Iterable, Set
from pathlib import Path, PureWindowsPath

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from locators.elements_page_locators import CheckBoxPageLocators, DynamicPropertiesLocators, RadioButtonPageLocators, TextBoxPageLocators, WebTablePageLocators, ButtonsPageLocators, LinksPageLocators, UploadAndDownloadPageLocators
from pages.base_page import BasePage
from generator.generator import generated_file, generated_person


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


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    def click_on_the_button(self):
        self.find_is_visible(self.locators.CLICK_ME_BUTTON).click()
        return self.find_is_present(self.locators.CLICK_ME_MESSAGE).text
    
    def double_click_on_the_button(self):
        self.action_double_click(self.find_is_visible(self.locators.DOUBLE_CLICK_BUTTON))
        return self.find_is_present(self.locators.DOUBLE_CLICK_MESSAGE).text
    
    def right_click_on_the_button(self):
        self.action_right_click(self.find_is_visible(self.locators.RIGHT_CLICK_BUTTON))
        return self.find_is_present(self.locators.RIGHT_CLICK_MESSAGE).text

        
class LinksPage(BasePage):
    locators = LinksPageLocators()

    def check_new_tab_simple_link(self):
        simple_link = self.find_is_visible(self.locators.SIMPLE_LINK)
        link_href = simple_link.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            simple_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return str(link_href), str(url)
        else:
            return request.status_code
    
    def check_broken_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.find_is_present(self.locators.BAD_REQUEST).click()
        else:
            return str(request.status_code)
            
class UploadAndDownloadPage(BasePage):
    locators = UploadAndDownloadPageLocators()
    def upload_file(self):
        file_name, path = generated_file()
        self.find_is_visible(self.locators.UPLOAD_FILE_INPUT).send_keys(path)
        uploaded_file_path = self.find_is_visible(self.locators.UPLOAD_FILE_PATH).text.split("\\")[-1].strip()
        #uploaded_file_path = PureWindowsPath(self.find_is_visible(self.locators.UPLOAD_FILE_PATH).text).name
        os.remove(path)
        print(f"Uploaded file name: {file_name}, Uploaded file path: {uploaded_file_path}")
        return file_name, uploaded_file_path


    #def download_file(self):
    #    href = self.find_is_present(self.locators.DOWNLOAD_BUTTON).get_attribute('href')
    #    if 'base64,' not in href:
    #        raise ValueError("В href нет base64-данных")
    #    base64_data = href.split('base64,', 1)[1]
    #    file_bytes = base64.b64decode(base64_data)
    #    file_name = f"test_file_{uuid.uuid4().hex}.jpg"
    #    file_path = os.path.join('/home/muhammad/Dev/qa-portfolio/file_for_tests', file_name)
    #    with open(file_path, 'wb') as file:
    #        file.write(file_bytes)
    #    file_size = os.path.getsize(file_path)
    #    if file_size == 0:
    #        raise AssertionError("Скачанный файл пустой")
    #    return file_path, file_name, file_size


    def download_file(self, timeout=10):
        download_dir = Path("file_for_tests").resolve()
        download_dir.mkdir(parents=True, exist_ok=True)
        before_files = {file.name for file in download_dir.iterdir()}

        self.find_is_visible(self.locators.DOWNLOAD_BUTTON).click()

        file_path = WebDriverWait(self.driver, timeout, poll_frequency=0.5).until(
            lambda _: next(
                (
                    file for file in download_dir.iterdir()
                    if file.name not in before_files
                    and file.is_file()
                    and file.suffix != ".crdownload"
                ),
                False
            ),
            message="Файл не был скачан за отведённое время"
        )

        file_size = file_path.stat().st_size
        if file_size == 0:
            raise AssertionError("Скачанный файл пустой")

        return str(file_path), file_path.name, file_size
    

    def delete_downloaded_file(self, file_path):
        if os.path.exists(file_path):
            os.remove(file_path)

class DynamicPropertiesPage(BasePage):
    locators = DynamicPropertiesLocators()

    def check_color_change(self, timeout=10):
        button = self.find_is_visible(self.locators.COLOR_CHANGE_BUTTON)
        color_before = button.value_of_css_property('color')

        WebDriverWait(self.driver, timeout).until(
            lambda driver: self.find_is_visible(self.locators.COLOR_CHANGE_BUTTON)
            .value_of_css_property('color') != color_before,
            message=f"Цвет кнопки не изменился за {timeout} секунд"
        )

        color_after = self.find_is_visible(self.locators.COLOR_CHANGE_BUTTON).value_of_css_property('color')
        return color_before, color_after

    def check_appear_button(self):
        try:
            self.find_is_visible(self.locators.VISIBLE_AFTER_BUTTON)
        except TimeoutException:
            return False
        return True
    
    def enable_button(self):
        try:
            button = self.find_is_visible(self.locators.ENABLE_BUTTON)
            return button.is_enabled()
        except TimeoutException:
            return False
    