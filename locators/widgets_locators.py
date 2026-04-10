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

class DatePickerPageLocators:
    DATE_INPUT = (By.CSS_SELECTOR, 'input[id="datePickerMonthYearInput"]')
    DATE_SELECT_MONTH = (By.CSS_SELECTOR, 'select[class="react-datepicker__month-select"]')
    DATE_SELECT_YEAR = (By.CSS_SELECTOR, 'select[class="react-datepicker__year-select"]')
    DATE_SELECT_DAY_LIST = (By.CSS_SELECTOR, 'div.react-datepicker__day:not(.react-datepicker__day--outside-month)')

    DATE_AND_TIME_INPUT = (By.CSS_SELECTOR, 'input[id="dateAndTimePickerInput"]')
    DATE_AND_TIME_SELECT_MONTH = (By.CSS_SELECTOR, 'button[class="react-datepicker__month-read-view"]')
    DATE_AND_TIME_SELECT_MONTH_LIST = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-option"]')
    DATE_AND_TIME_SELECT_YEAR = (By.CSS_SELECTOR, 'button[class="react-datepicker__year-read-view"]')
    DATE_AND_TIME_SELECT_YEAR_LIST = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-option"]')
    DATE_AND_TIME_SELECT_HOUR_LIST = (By.CSS_SELECTOR, 'li[class="react-datepicker__time-list-item "]')

class SliderPageLocators:
    INPUT_SLIDER = (By.CSS_SELECTOR, 'input[id="slider"]')
    SLIDER_VALUE = (By.CSS_SELECTOR, 'input[id="sliderValue"]')

class ProgressBarPageLocators:
    PROGRESS_BAR_BUTTON = (By.CSS_SELECTOR, 'button[id="startStopButton"]')
    PROGRESS_BAR_VALUE = (By.CSS_SELECTOR, 'div[role="progressbar"]')

class TabsPageLocators:
    TABS_WHAT = (By.CSS_SELECTOR, 'button[id="demo-tab-what"]')
    TABS_WHAT_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-what"]')
    TABS_ORIGIN = (By.CSS_SELECTOR, 'button[id="demo-tab-origin"]')
    TABS_ORIGIN_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-origin"]')
    TABS_USE = (By.CSS_SELECTOR, 'button[id="demo-tab-use"]')
    TABS_USE_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-use"]')
    TABS_MORE = (By.CSS_SELECTOR, 'button[id="demo-tab-more"]')
    TABS_MORE_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-more"]')