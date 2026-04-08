
import time
from pages.widgets_page import AccordianPage, AutoCompletePage


class TestWidgets:
    class TestAccordianPage:
        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open() 
            first_accordian = accordian_page.check_accordian(accordian_n='first')
            second_accordian = accordian_page.check_accordian(accordian_n='second')
            third_accordian = accordian_page.check_accordian(accordian_n='third')
            assert first_accordian == ['What is Lorem Ipsum?', 574], "First accordian is not correct"
            assert second_accordian == ['Where does it come from?', 1059], "Second accordian is not correct"
            assert third_accordian == ['Why do we use it?', 613], "Third accordian is not correct"
    
    class TestAutoCimpletePage:
        def test_fill_multi_auto_complete(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            colors = auto_complete_page.fill_input_multi()
            colors_result = auto_complete_page.check_color_in_multi()
            assert colors == colors_result, "Colors in multi auto complete is not correct"

        def test_remove_value_from_multi(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            auto_complete_page.fill_input_multi()
            before, after = auto_complete_page.remove_value_from_multi()
            assert before != after, "Value was not removed from multi auto complete"

        def test_complete_removal_of_value_from_multi(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            auto_complete_page.fill_input_multi()
            count_value_after = auto_complete_page.complete_removal_of_value_from_multi()
            assert count_value_after == 0, "Values were not removed from multi auto complete"

        def test_fill_single_auto_complete(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            color = auto_complete_page.fill_single_input()
            color_result = auto_complete_page.check_color_in_single()
            assert color == color_result, "Color in single auto complete is not correct"

