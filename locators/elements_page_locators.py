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

class WebTablePageLocators:
    #Add person form
    ADD_BUTTON = (By.CSS_SELECTOR, 'button[id="addNewRecordButton"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'span[title="Delete"]')

    FIRST_NAME_INPUT = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    AGE_INPUT = (By.CSS_SELECTOR, 'input[id="age"]')
    SALARY_INPUT = (By.CSS_SELECTOR, 'input[id="salary"]')
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, 'input[id="department"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[id="submit"]')

    #Tables
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, 'table.table tbody tr')
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[id="searchBox"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'span[title="Delete"]')
    ROW_PARENT = (By.XPATH, "./ancestor::tr")
    COUNT_ROW_LIST = (By.CSS_SELECTOR, 'select[class="form-control"]')
    COUNT_ACTIVE_ROW = (By.CSS_SELECTOR, 'select.form-control option:checked')

    #Update person info
    UPDATE_BUTTON = (By.CSS_SELECTOR, 'span[title="Edit"]')

class ButtonsPageLocators:
    DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, 'button[id="doubleClickBtn"]')
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, 'button[id="rightClickBtn"]')
    CLICK_ME_BUTTON = (By.XPATH, "//button[text()='Click Me']")
    DOUBLE_CLICK_MESSAGE = (By.CSS_SELECTOR, 'p[id="doubleClickMessage"]')
    RIGHT_CLICK_MESSAGE = (By.CSS_SELECTOR, 'p[id="rightClickMessage"]')
    CLICK_ME_MESSAGE = (By.CSS_SELECTOR, 'p[id="dynamicClickMessage"]')

class LinksPageLocators:
    SIMPLE_LINK = (By.CSS_SELECTOR, 'a[id="simpleLink"]')
    BAD_REQUEST = (By.CSS_SELECTOR, 'a[id="bad-request"]')

class UploadAndDownloadPageLocators:
    UPLOAD_FILE_INPUT = (By.CSS_SELECTOR, 'input[id="uploadFile"]')
    UPLOAD_FILE_PATH = (By.CSS_SELECTOR, 'p[id="uploadedFilePath"]')
    DOWNLOAD_BUTTON = (By.CSS_SELECTOR, 'a[id="downloadButton"]')