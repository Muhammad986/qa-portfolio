from selenium.webdriver.common.by import By

class BrowserWindowsPageLocators:
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, "#tabButton")#button[id="tabButton"]
    TEXT_NEW_TAB = (By.CSS_SELECTOR, "#sampleHeading")
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, "#windowButton")
    TEXT_NEW_WINDOW = (By.CSS_SELECTOR, "#sampleHeading")

    
class AlertsPageLocators:
    # Alerts
    SEE_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='alertButton']")
    APPEAR_ALERT_AFTER_5_SEC_BUTTON = (By.CSS_SELECTOR, "button[id='timerAlertButton']")
    CONFIRM_BOX_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='confirmButton']")
    CONFIRM_RESULT = (By.CSS_SELECTOR, 'span[id="confirmResult"]')
    PROMPT_BOX_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="promtButton"]')
    PROMPT_RESULT = (By.CSS_SELECTOR, 'span[id="promptResult"]')

class FramesPageLocators:
    FRAME_1 = (By.CSS_SELECTOR, 'iframe[id="frame1"]')
    FRAME_2 = (By.CSS_SELECTOR, 'iframe[id="frame2"]')
    TEXT_FRAME = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')

class NestedFramesPageLocators:
    PARENT_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame1"]')
    CHILD_FRAME = (By.CSS_SELECTOR, 'iframe[srcdoc="<p>Child Iframe</p>"]')
    TEXT_PARENT_FRAME = (By.CSS_SELECTOR, 'body')
    TEXT_CHILD_FRAME = (By.CSS_SELECTOR, 'body')

class ModalDialogsPageLocators:
    SMALL_MODAL_BUTTON = (By.CSS_SELECTOR, 'button[id="showSmallModal"]')
    LARGE_MODAL_BUTTON = (By.CSS_SELECTOR, 'button[id="showLargeModal"]')
    TEXT_MODAL = (By.CSS_SELECTOR, 'div.modal-body')
    TITLE_MODAL = (By.CSS_SELECTOR, 'div.modal-title')
    CLOSE_SMALL_MODAL_BUTTON = (By.CSS_SELECTOR, 'button[id="closeSmallModal"]')
    CLOSE_LARGE_MODAL_BUTTON = (By.CSS_SELECTOR, 'button[id="closeLargeModal"]')