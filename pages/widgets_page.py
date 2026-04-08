import time

from faker.generator import random
from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys


from generator.generator import generated_color
from locators.widgets_locators import AccordianPageLocators, AutoCompleteLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, accordian_n: str):
        accordian = {'first': {
                        'title': self.locators.SECTION_FIRST,
                        'content': self.locators.SECTION_CONTENT_FIRST
                    },
                     'second': {
                        'title': self.locators.SECTION_SECOND,
                        'content': self.locators.SECTION_CONTENT_SECOND
                    },
                     'third': {
                        'title': self.locators.SECTION_THIRD,
                        'content': self.locators.SECTION_CONTENT_THIRD
                    }
                    }
        try:    
            section_title = self.find_is_visible(accordian[accordian_n]['title'])
            section_title.click()
            section_content = self.find_is_visible(accordian[accordian_n]['content'])

        except TimeoutException: 
            section_title = self.find_is_visible(accordian[accordian_n]['title'])
            section_title.click()
            section_content = self.find_is_visible(accordian[accordian_n]['content'])

        return [section_title.text, len(section_content.text)]


class AutoCompletePage(BasePage):
    locators = AutoCompleteLocators()
    
    def fill_input_multi(self):
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 5))
        for color in colors:
            input_multi = self.find_is_clickable(self.locators.MULTI_INPUT)
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
        return colors
    
    def remove_value_from_multi(self):
        count_value_before = len(self.find_are_visible(self.locators.MULTI_VALUE))
        remove_button_list = self.find_are_visible(self.locators.MULTI_VALUE_REMOVE)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.find_are_visible(self.locators.MULTI_VALUE))
        return count_value_before, count_value_after
    
    def check_color_in_multi(self):
        color_list = self.find_are_visible(self.locators.MULTI_VALUE)
        colors = [color.text for color in color_list]
        return colors
    
    def complete_removal_of_value_from_multi(self):
        self.find_is_clickable(self.locators.MULTI_VALUE_ALL_REMOVE).click()
        count_value_after = len(self.driver.find_elements(*self.locators.MULTI_VALUE))
        return count_value_after
    

    def  fill_single_input(self):
        color = random.choice(next(generated_color()).color_name)
        input_single = self.find_is_clickable(self.locators.SINGLE_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color
    
    def check_color_in_single(self):
        color_result = self.find_is_visible(self.locators.SINGLE_CONTAINER).text
        return color_result
