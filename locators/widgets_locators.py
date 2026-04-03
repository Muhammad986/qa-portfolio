from selenium.webdriver.common.by import By

class AccordianPageLocators:
    SECTION_FIRST = (By.XPATH, "(//button[contains(@class, 'accordion-button')])[1]")
    SECTION_CONTENT_FIRST = (By.XPATH, "(//div[contains(@class, 'accordion-body')])[1]")
    SECTION_SECOND = (By.XPATH, "(//button[contains(@class, 'accordion-button')])[2]")
    SECTION_CONTENT_SECOND = (By.XPATH, "(//div[contains(@class, 'accordion-body')])[2]")
    SECTION_THIRD = (By.XPATH, "(//button[contains(@class, 'accordion-button')])[3]")
    SECTION_CONTENT_THIRD = (By.XPATH, "(//div[contains(@class, 'accordion-body')])[3]")
