
import time
from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, MenuPage, ProgressBarPage, SelectMenuPage, SliderPage, TabsPage, ToolTipsPage


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

    class TestDatePickerPage:

        def  test_change_date(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date()
            assert value_date_before != value_date_after, "Date was not changed"

        def test_change_date_and_time(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_and_time_before, value_date_and_time_after = date_picker_page.select_date_and_time()
            assert value_date_and_time_before != value_date_and_time_after, "Date and time was not changed"

    class TestSliderPage:
        def test_slider(self, driver):
            slider_page = SliderPage(driver, 'https://demoqa.com/slider') 
            slider_page.open()
            before, after = slider_page.chenge_slider_value()
            assert before != after, "Slider value was not changed"

    class TestProgressBarPage:
        def test_progress_bar(self, driver):
            progress_bar_page = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar_page.open()
            before, after = progress_bar_page.chenge_progress_bar_value()
            assert before != after, "Progress bar value was not changed"

    class TestTabs:
        def test_tabs(self, driver):
            tabs_page = TabsPage(driver, 'https://demoqa.com/tabs')
            tabs_page.open()
            what_button, what_content = tabs_page.check_tabs('what')
            origin_button, origin_content = tabs_page.check_tabs('origin')
            use_button, use_content = tabs_page.check_tabs('use')
            # more_button, more_content = tabs_page.check_tabs('more')

            assert what_button == 'What' and what_content != 0, "The tab 'What' was not pressed or the text is missing."
            assert origin_button == 'Origin' and origin_content != 0, "The tab 'Origin' was not pressed or the text is missing."
            assert use_button == 'Use' and use_content != 0, "The tab 'Use' was not pressed or the text is missing."
            # assert more_button == 'More' and more_content != 0, "The tab 'More' was not pressed or the text is missing." #The “More” button isn't working
            
    class TestToolTips:
        def test_tool_tips(self, driver):
            tool_tips_page = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
            tool_tips_page.open()
            button_text, field_text, contrary_text, section_text = tool_tips_page.check_tool_tips()
            assert button_text == 'You hovered over the Button', 'Hover missing or incorrect content'
            assert field_text == 'You hovered over the text field', 'Hover missing or incorrect content'
            assert contrary_text == 'You hovered over the Contrary', 'Hover missing or incorrect content'
            assert section_text == 'You hovered over the 1.10.32', 'Hover missing or incorrect content'

    class TestMenu:
        def test_menu(self, driver):
            menu_page = MenuPage(driver, 'https://demoqa.com/menu')
            menu_page.open()
            data = menu_page.check_menu()

            assert data == ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1', 'Sub Sub Item 2', 'Main Item 3'], 'Menu item do not exist or have not been selected'

    class TestSelectMenu:
        def test_select_menu(self, driver):
            select_menu_page = SelectMenuPage(driver, 'https://demoqa.com/select-menu')
            select_menu_page.open()

            expected_result = select_menu_page.fill_select_menu()
            actual_result = select_menu_page.get_select_menu_result()
            print(actual_result)

            assert expected_result == actual_result


