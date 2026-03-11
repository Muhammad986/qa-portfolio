from selenium.webdriver.common.by import By

class TextBoxPageLocators:

    #form fields
    FULL_NAME = (By.CSS_SELECTOR, 'input[id="userName"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="permanentAddress"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[id="submit"]')

    #created form
    CREATED_FULL_NAME = (By.CSS_SELECTOR, '#output #name')
    CREATED_EMAIL = (By.CSS_SELECTOR, '#output #email')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#output #permanentAddress')

class CheckBoxPageLocators:

    SWITCHER_CLOSE = (By.CSS_SELECTOR, "span.rc-tree-switcher.rc-tree-switcher_close")
    ITEM_LIST = (By.XPATH, "//span[contains(@class, 'rc-tree-title')]")
    CHECKBOX_LIST = (By.XPATH, "//span[contains(@class, 'rc-tree-checkbox')]")
    CHECKED_ITEMS = (By.XPATH, '//span[contains(@aria-checked, "true")]')
    TITLE_ITEM = (By.XPATH, "./..//span[contains(@class, 'rc-tree-title')]")
    OUTPUT_RESULT = (By.CSS_SELECTOR, 'span.text-success')

class RadioButtonPageLocators:
    YES_RADIO = (By.CSS_SELECTOR, 'label[for="yesRadio"]')
    IMPRESSIVE_RADIO = (By.CSS_SELECTOR, 'label[for="impressiveRadio"]')
    NO_RADIO = (By.CSS_SELECTOR, 'label[for="noRadio"]')
    OUTPUT_RESULT = (By.CSS_SELECTOR, 'span.text-success')