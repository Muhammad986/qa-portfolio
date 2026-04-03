import time

from selenium.common import TimeoutException
from locators.widgets_locators import AccordianPageLocators
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
