
import time

from pages.alert_frame_windows_page import BrowserWindowsPage, TestAlertsPage


class TestAlertFrameWindows:    
    class TestBrowserWindows:
        
        def test_new_tab(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_windows_page.open()
            text = browser_windows_page.check_opened_new_tab()
            assert text == 'This is a sample page', "Text in new tab does not match expected value"

        def test_new_window(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_windows_page.open()
            text = browser_windows_page.check_opened_new_window()
            assert text == 'This is a sample page', "Text in new window does not match expected value"


    class TestAlertsPage:
        def test_see_alert(self, driver):
            browser_windows_page = TestAlertsPage(driver, 'https://demoqa.com/alerts')
            browser_windows_page.open()
            alert_text = browser_windows_page.check_see_alert()
            assert alert_text == 'You clicked a button', "Alert text does not match expected value"

        def test_see_alert_after_5_sec(self, driver):
            browser_windows_page = TestAlertsPage(driver, 'https://demoqa.com/alerts')
            browser_windows_page.open()
            alert_text = browser_windows_page.check_see_alert_after_5_sec()
            assert alert_text == 'This alert appeared after 5 seconds', "Alert text does not match expected value"

        def test_confirm_box_alert(self, driver):
            browser_windows_page = TestAlertsPage(driver, 'https://demoqa.com/alerts')
            browser_windows_page.open()
            text_result = browser_windows_page.check_confirm_box_alert()
            print(text_result)
            assert text_result == 'You selected Ok' or text_result == 'You selected Cancel', "Confirm result text does not match expected value"

        def test_prompt_box_alert(self, driver):
            input_text = 'Soska'
            browser_windows_page = TestAlertsPage(driver, 'https://demoqa.com/alerts')
            browser_windows_page.open()
            text_result = browser_windows_page.check_prompt_box_alert(input_text)
            assert text_result == f'You entered {input_text}', "Prompt result text does not match expected value"