import time

from faker.generator import random
from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait


from generator.generator import generated_color, generated_date
from locators.widgets_locators import AccordianPageLocators, AutoCompleteLocators, DatePickerPageLocators, MenuPageLocators, ProgressBarPageLocators, SelectMenuPageLocators, SliderPageLocators, TabsPageLocators, ToolTipsPageLocators
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
    
class TabsPage(BasePage):
    locators = TabsPageLocators()
    def check_tabs(self, tabs_n):
        tabs = {
            'what': {
                'button': self.locators.TABS_WHAT,
                'content': self.locators.TABS_WHAT_CONTENT
            },
            'origin': {
                'button': self.locators.TABS_ORIGIN,
                'content': self.locators.TABS_ORIGIN_CONTENT
            },
            'use': {
                'button': self.locators.TABS_USE,
                'content': self.locators.TABS_USE_CONTENT
            },
            'more': {
                'button': self.locators.TABS_MORE,
                'content': self.locators.TABS_MORE_CONTENT
            }
        }

        tab_button = self.find_is_visible(tabs[tabs_n]['button'])
        tab_button.click()
        tab_content = self.find_is_visible(tabs[tabs_n]['content'])
        return tab_button.text, len(tab_content.text)
    
class ToolTipsPage(BasePage):
    locators = ToolTipsPageLocators()

    def get_text_from_tool_tips(self, hover_elem, timeout=5):
        element = self.find_is_present(hover_elem, timeout)
        self.go_to_element(element)
        element = self.find_is_visible_no_scroll(hover_elem, timeout)

        self.action_move_to_element(element)
        #Дублируем hover через JS. Это страховка от нестабильного ActionChains
        self.driver.execute_script(
            "arguments[0].dispatchEvent(new MouseEvent('mouseover', {bubbles: true}));",
            element
        )

        tooltip_id = wait(self.driver, timeout).until(
            lambda driver: element.get_attribute("aria-describedby") or False
        )

        tooltip_locator = (By.CSS_SELECTOR, f'div[id="{tooltip_id}"] .tooltip-inner')

        return wait(self.driver, timeout).until(
            lambda driver: driver.find_element(*tooltip_locator).text.strip() or False
        )

    def check_tool_tips(self):
        tool_tip_text_button = self.get_text_from_tool_tips(self.locators.BUTTON)
        tool_tip_text_field = self.get_text_from_tool_tips(self.locators.FIELD)
        tool_tip_text_contrary = self.get_text_from_tool_tips(self.locators.CONTRARY_LINK)
        tool_tip_text_section = self.get_text_from_tool_tips(self.locators.SECTION_LINK)

        return (
            tool_tip_text_button,
            tool_tip_text_field,
            tool_tip_text_contrary,
            tool_tip_text_section
        )
    
class MenuPage(BasePage):
    locators = MenuPageLocators()

    def check_menu(self):
        menu_item_list = self.find_are_present(self.locators.MENU_ITEM_LIST)
        data = []
        
        for item in menu_item_list:
            self.action_move_to_element(item)
            data.append(item.text)
        return data
    

class SelectMenuPage(BasePage):
    locators = SelectMenuPageLocators()

    SELECT_VALUE_OPTIONS = [
        "Group 1, option 1",
        "Group 1, option 2",
        "Group 2, option 1",
        "Group 2, option 2",
        "A root option"
    ]
    SELECT_ONE_OPTIONS = ["Dr.", "Mr.", "Mrs.", "Ms.", "Prof.", "Other"]
    MULTISELECT_OPTIONS = ["Red", "Blue", "Green", "Black"]

    def open_react_select(self, container_locator, timeout=5):
        container = self.find_is_clickable(container_locator, timeout)
        self.go_to_element(container)

        try:
            container.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", container)

    def select_react_option(self, container_locator, input_locator, value, timeout=5):
        self.open_react_select(container_locator, timeout)

        input_element = self.find_is_visible_no_scroll(input_locator, timeout)
        input_element.send_keys(value)

        option_locator = (
            By.XPATH,
            f"//div[@role='option' and normalize-space()='{value}']"
        )
        self.find_is_clickable(option_locator, timeout).click()
        return value

    def select_random_react_option(self, container_locator, input_locator, values, timeout=5):
        value = random.choice(values)
        return self.select_react_option(container_locator, input_locator, value, timeout)

    def select_random_html_option(self, select_locator):
        select = Select(self.find_is_visible(select_locator))
        value = random.choice([option.text for option in select.options])
        select.select_by_visible_text(value)
        return value

    def select_random_react_multi_options(self, container_locator, input_locator, values, timeout=5):
        selected_values = random.sample(values, k=random.randint(1, min(2, len(values))))
        for value in selected_values:
            self.select_react_option(container_locator, input_locator, value, timeout)
        return selected_values

    def get_react_single_value(self, container_locator):
        container = self.find_is_visible(container_locator)
        return container.find_element(
            By.XPATH,
            ".//div[contains(@class, 'singleValue')]"
        ).text

    def get_react_multi_values(self, container_locator):
        container = self.find_is_visible(container_locator)
        values = container.find_elements(
            By.XPATH,
            ".//div[contains(@class, 'multiValue')]/div[1]"
        )
        return [value.text for value in values]

    def fill_select_menu(self):
        return {
            "select_value": self.select_random_react_option(
                self.locators.SELECT_VALUE,
                self.locators.SELECT_VALUE_INPUT,
                self.SELECT_VALUE_OPTIONS
            ),
            "select_one": self.select_random_react_option(
                self.locators.SELECT_ONE,
                self.locators.SELECT_ONE_INPUT,
                self.SELECT_ONE_OPTIONS
            ),
            "old_style": self.select_random_html_option(
                self.locators.OLD_STYLE_SELECT_INPUT
            ),
            "multi_select": self.select_random_react_multi_options(
                self.locators.MULTISELECT_DROP_DOWN,
                self.locators.MULTISELECT_DROP_DOWN_INPUT,
                self.MULTISELECT_OPTIONS
            ),
            "standard_select": self.select_random_html_option(
                self.locators.STANDARD_MUTISELECT_INPUT
            )
        }

    def get_select_menu_result(self):
        old_style_select = Select(self.find_is_visible(self.locators.OLD_STYLE_SELECT_INPUT))
        standard_select = Select(self.find_is_visible(self.locators.STANDARD_MUTISELECT_INPUT))

        return {
            "select_value": self.get_react_single_value(self.locators.SELECT_VALUE),
            "select_one": self.get_react_single_value(self.locators.SELECT_ONE),
            "old_style": old_style_select.first_selected_option.text,
            "multi_select": self.get_react_multi_values(self.locators.MULTISELECT_DROP_DOWN),
            "standard_select": standard_select.first_selected_option.text
        }
