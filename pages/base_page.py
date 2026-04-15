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
    
    def find_is_visible_no_scroll(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    def find_is_invisible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
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

    def action_drag_and_drop(self, element, x_coordinate, y_coordinate):
        self.go_to_element(element)
        ActionChains(self.driver) \
            .move_to_element(element) \
            .click_and_hold(element) \
            .pause(0.2) \
            .move_by_offset(x_coordinate, y_coordinate) \
            .pause(0.2) \
            .release() \
            .perform()
    

    def action_drag_and_drop_to_element(self, what, where, hold_pause=0.2, move_pause=0.2):
        self.go_to_element(what)
        self.go_to_element(where)
    
        action = ActionChains(self.driver)
        action.move_to_element(what)
        action.click_and_hold(what)
        action.pause(hold_pause)
        action.move_to_element(where)
        action.pause(move_pause)
        action.release(where)
        action.perform()
        
    def scroll_to_page_bottom(self, timeout=5):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        wait(self.driver, timeout).until(
            lambda d: d.execute_script(
                "return Math.ceil(window.innerHeight + window.pageYOffset) >= document.body.scrollHeight"
            )
        )


    def action_move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

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
    
    def get_frame_data(self, frame_locator, text_locator, switch_back="default"):
        frame = self.find_is_present(frame_locator)
        width = frame.value_of_css_property("width")
        height = frame.value_of_css_property("height")



        self.driver.switch_to.frame(frame)
        text = self.find_is_visible(text_locator).text

        if switch_back == "default":
            self.driver.switch_to.default_content()
        elif switch_back == "parent":
            self.driver.switch_to.parent_frame()
        elif switch_back is None:
            pass
        else:
            raise ValueError(f"Unsupported switch_back value: {switch_back}")

        return [text, width, height]

    