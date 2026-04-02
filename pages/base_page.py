from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def find_is_visible(self, locator, timeout=5):
        self.go_to_element(self.driver.find_element(*locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    def find_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))
    
    def find_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))
    
    def find_are_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
    
    def find_is_not_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
    
    def find_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
    
    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)

    def action_double_click(self, element):
        ActionChains(self.driver).double_click(element).perform()

    def action_right_click(self, element):
        ActionChains(self.driver).context_click(element).perform()

    def click_and_switch_to_new_window(self, locator, timeout=10):
        old_handles = set(self.driver.window_handles)
        parent_handle = self.driver.current_window_handle
    
        self.find_is_clickable(locator, timeout).click()
    
        wait(self.driver, timeout).until(
            lambda driver: len(set(driver.window_handles) - old_handles) > 0
        )
    
        new_handle = (set(self.driver.window_handles) - old_handles).pop()
        self.driver.switch_to.window(new_handle)
    
        return parent_handle, new_handle
    

    def click_and_handle_alert(self, locator, timeout=10, action="accept", input_text=None):
        self.find_is_clickable(locator, timeout).click()
    
        alert = wait(self.driver, timeout).until(EC.alert_is_present())
        alert_text = alert.text
    
        if input_text is not None:
            alert.send_keys(input_text)
    
        if action == "accept":
            alert.accept()
        elif action == "dismiss":
            alert.dismiss()
        else:
            raise ValueError(f"Unsupported alert action: {action}")
    
        return alert_text
    
    