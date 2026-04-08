from selenium.webdriver.common.by import By

class AccordianPageLocators:
    SECTION_FIRST = (By.XPATH, "(//button[contains(@class, 'accordion-button')])[1]")
    SECTION_CONTENT_FIRST = (By.XPATH, "(//div[contains(@class, 'accordion-body')])[1]")
    SECTION_SECOND = (By.XPATH, "(//button[contains(@class, 'accordion-button')])[2]")
    SECTION_CONTENT_SECOND = (By.XPATH, "(//div[contains(@class, 'accordion-body')])[2]")
    SECTION_THIRD = (By.XPATH, "(//button[contains(@class, 'accordion-button')])[3]")
    SECTION_CONTENT_THIRD = (By.XPATH, "(//div[contains(@class, 'accordion-body')])[3]")

class AutoCompleteLocators:
    MULTI_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteMultipleInput"]')
    MULTI_VALUE = (By.CSS_SELECTOR, 'div.auto-complete__multi-value')
    MULTI_VALUE_REMOVE = (By.CSS_SELECTOR, 'div.auto-complete__multi-value svg path')
    MULTI_VALUE_ALL_REMOVE = (By.CSS_SELECTOR, 'div.auto-complete__indicator svg path')

    SINGLE_CONTAINER = (By.CSS_SELECTOR, 'div[id="autoCompleteSingleContainer"]')
    SINGLE_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteSingleInput"]')

