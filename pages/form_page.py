import os

from selenium.webdriver.common.keys import Keys
from generator.generator import generate_random_date, generated_file, generated_person, generated_subject
from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators

class FormPage(BasePage):
    locators = FormPageLocators()

    def  fill_form_fields(self):
        person = next(generated_person())
        _, path = generated_file()

        # Fill in the form fields
        self.find_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(person.first_name)
        self.find_is_visible(self.locators.LAST_NAME_INPUT).send_keys(person.last_name)
        self.find_is_visible(self.locators.EMAIL_INPUT).send_keys(person.email)
        self.find_is_visible(self.locators.GENDER).click()
        self.find_is_visible(self.locators.MOBILE_INPUT).send_keys(person.mobile)
        #We don't check the date of birth, that part is broken.
        #self.find_is_visible(self.locators.DATE_OF_BIRTH_INPUT).send_keys(person.date_of_birth)
        #self.find_is_visible(self.locators.DATE_OF_BIRTH_INPUT).send_keys(Keys.ENTER)
        self.find_is_visible(self.locators.SUBJECTS_INPUT).send_keys(generated_subject())
        self.find_is_visible(self.locators.SUBJECTS_INPUT).send_keys(Keys.ENTER)
        self.find_is_visible(self.locators.HOBBIES).click()
        self.find_is_visible(self.locators.UPLOAD_PICTURE).send_keys(path)
        os.remove(path)
        self.find_is_visible(self.locators.CURRENT_ADDRESS).send_keys(person.current_address)
        self.find_is_visible(self.locators.SELECT_STATE).click()
        self.find_is_visible(self.locators.SELECT_STATE_INPUT).send_keys(Keys.ENTER)
        self.find_is_visible(self.locators.SELECT_CITY).click()
        self.find_is_visible(self.locators.SELECT_CITY_INPUT).send_keys(Keys.ENTER)
        self.find_is_visible(self.locators.SUBMIT_BUTTON).click()
        return person

    def form_result(self):
        result_list = self.find_are_present(self.locators.TABLE_RESULT)
        data =[]
        for element in result_list:
            self.go_to_element(element)
            data.append(element.text)
        return data