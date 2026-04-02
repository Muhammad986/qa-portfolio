
import time

from pages.alert_frame_windows_page import BrowserWindowsPage


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