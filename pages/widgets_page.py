import time

from faker.generator import random
from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


from generator.generator import generated_color, generated_date
from locators.widgets_locators import AccordianPageLocators, AutoCompleteLocators, DatePickerPageLocators, ProgressBarPageLocators, SliderPageLocators
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
    
class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()

    def select_date(self):
        date = next(generated_date())
        input_date = self.find_is_visible(self.locators.DATE_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.set_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.set_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.date)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after

    def select_date_and_time(self):
        date = next(generated_date())
        input_date_and_time = self.find_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_and_time_before = input_date_and_time.get_attribute('value')
        input_date_and_time.click()
        self.find_is_visible(self.locators.DATE_AND_TIME_SELECT_MONTH).click()
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_SELECT_MONTH_LIST, date.month)
        self.find_is_visible(self.locators.DATE_AND_TIME_SELECT_YEAR).click()
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_SELECT_YEAR_LIST, '2024')
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.date)
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_SELECT_HOUR_LIST, date.time)
        value_date_and_time_after = input_date_and_time.get_attribute('value')
        return value_date_and_time_before, value_date_and_time_after

    def set_date_by_text(self, element, value):
        select = Select(self.find_is_visible(element))
        select.select_by_visible_text(value)

    def set_date_item_from_list(self, elements, value):
        item_list = self.find_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break

class SliderPage(BasePage):
    locators = SliderPageLocators()

    def chenge_slider_value(self):
        value_before = self.find_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        slider = self.find_is_visible(self.locators.INPUT_SLIDER)
        self.action_drag_and_drop(slider, x_coordinate=random.randint(0, 100), y_coordinate=0)
        value_after = self.find_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        return value_before, value_after

class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators() 
    def chenge_progress_bar_value(self):
        value_before = self.find_is_present(self.locators.PROGRESS_BAR_VALUE).get_attribute('aria-valuenow')
        progress_bar_button = self.find_is_clickable(self.locators.PROGRESS_BAR_BUTTON)
        progress_bar_button.click()
        time.sleep(random.randint(2, 5))
        progress_bar_button.click()
        value_after = self.find_is_present(self.locators.PROGRESS_BAR_VALUE).get_attribute('aria-valuenow')
        return value_before, value_after