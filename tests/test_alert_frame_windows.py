
import time

import allure

from pages.alert_frame_windows_page import BrowserWindowsPage, AlertsPage, FramesPage, ModalDialogsPage, NestedFramesPage

@allure.suite('Alerts, Frames and Windows')
class TestAlertFrameWindows:

    @allure.feature('BrowserWindowsPage') 
    class TestBrowserWindows:
        
        @allure.title('Test new tab')
        def test_new_tab(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_windows_page.open()
            text = browser_windows_page.check_opened_new_tab()
            assert text == 'This is a sample page', "Text in new tab does not match expected value"

        @allure.title('Test new window')
        def test_new_window(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_windows_page.open()
            text = browser_windows_page.check_opened_new_window()
            assert text == 'This is a sample page', "Text in new window does not match expected value"

    @allure.feature('AlertsPage')
    class TestAlertsPage:

        @allure.title('Test see alert')
        def test_see_alert(self, driver):
            browser_windows_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            browser_windows_page.open()
            alert_text = browser_windows_page.check_see_alert()
            assert alert_text == 'You clicked a button', "Alert text does not match expected value"

        @allure.title('Test alert after 5 seconds')
        def test_see_alert_after_5_sec(self, driver):
            browser_windows_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            browser_windows_page.open()
            alert_text = browser_windows_page.check_see_alert_after_5_sec()
            assert alert_text == 'This alert appeared after 5 seconds', "Alert text does not match expected value"

        @allure.title('Test confirm box alert')
        def test_confirm_box_alert(self, driver):
            browser_windows_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            browser_windows_page.open()
            text_result = browser_windows_page.check_confirm_box_alert()
            print(text_result)
            assert text_result == 'You selected Ok' or text_result == 'You selected Cancel', "Confirm result text does not match expected value"

        @allure.title('Test prompt box alert')
        def test_prompt_box_alert(self, driver):
            input_text = 'Soska'
            browser_windows_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            browser_windows_page.open()
            text_result = browser_windows_page.check_prompt_box_alert(input_text)
            assert text_result == f'You entered {input_text}', "Prompt result text does not match expected value"

    @allure.feature('FramePage')
    class TestFramesPage:

        @allure.title('Test frames')
        def test_frames(self, driver):
            frames_page = FramesPage(driver, 'https://demoqa.com/frames')
            frames_page.open()
            result_frame_1 = frames_page.check_frames('frame_1')
            result_frame_2 = frames_page.check_frames('frame_2')
            assert result_frame_1 == ['This is a sample page', '500px', '350px'] and result_frame_2 == ['This is a sample page', '100px', '100px'], "Frame text or dimensions do not match expected values"

    @allure.feature('NestedFramesPage')
    class TestNestedFramesPage:

        @allure.title('Test nested frames')
        def test_nested_frames(self, driver):
            nested_frames_page = NestedFramesPage(driver, 'https://demoqa.com/nestedframes')
            nested_frames_page.open()
            nested_frames_page.check_nested_frames()
            parent_frame, child_frame = nested_frames_page.check_nested_frames()
            assert parent_frame == ['Parent frame', '500px', '350px'] and child_frame == ['Child Iframe', '300px', '150px'], "Nested frame texts do not match expected values"

    @allure.feature('ModalDialogsPage')
    class TestModalDialogsPage:

        @allure.title('Test modal dialogs')
        def test_modal_dialogs(self, driver):
            modal_dialog_page = ModalDialogsPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialog_page.open()
            small_dialog = modal_dialog_page.check_small_modal_dialog()
            large_dialog = modal_dialog_page.check_large_modal_dialog()
            assert small_dialog == ['Small Modal', 47], "Small modal title or text length does not match expected values"
            assert large_dialog == ['Large Modal', 574], "Large modal title or text length does not match expected values"