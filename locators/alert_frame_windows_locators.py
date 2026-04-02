from selenium.webdriver.common.by import By

class BrowserWindowsPageLocators:
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, "#tabButton")#button[id="tabButton"]
    TEXT_NEW_TAB = (By.CSS_SELECTOR, "#sampleHeading")
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, "#windowButton")
    TEXT_NEW_WINDOW = (By.CSS_SELECTOR, "#sampleHeading")