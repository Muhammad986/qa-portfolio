

from pages.widgets_page import AccordianPage


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
