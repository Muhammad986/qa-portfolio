import random

from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait as wait

from pages.base_page import BasePage
from locators.interactions_page_locators import SortablePageLocators


class SortablePage(BasePage):
    locators = SortablePageLocators()

    def get_sortable_item(self, elements, timeout=5):
        def visible_items(driver):
            items = [item for item in driver.find_elements(*elements) if item.is_displayed()]
            return items if items else False

        item_list = wait(self.driver, timeout).until(visible_items)
        return [item.text.strip() for item in item_list]

    def get_sortable_item_element(self, elements, text, timeout=5):
        def visible_item_by_text(driver):
            for item in driver.find_elements(*elements):
                if item.is_displayed() and item.text.strip() == text:
                    return item
            return False

        return wait(self.driver, timeout).until(visible_item_by_text)

    def wait_for_new_order(self, elements, order_before, timeout=5):
        def order_changed(driver):
            current_order = self.get_sortable_item(elements, timeout)
            return current_order if current_order != order_before else False

        return wait(self.driver, timeout).until(order_changed)

    def swap_elements(self, elements, timeout=5, attempts=3):
        order_before = self.get_sortable_item(elements, timeout)

        source_index = random.randint(1, len(order_before) - 1)
        source_text = order_before[source_index]
        target_text = order_before[source_index - 1]

        for _ in range(attempts):
            item_what = self.get_sortable_item_element(elements, source_text, timeout)
            item_where = self.get_sortable_item_element(elements, target_text, timeout)

            self.action_drag_and_drop_to_element(item_what, item_where)

            try:
                order_after = self.wait_for_new_order(elements, order_before, timeout)
                return order_before, order_after
            except TimeoutException:
                continue

        return order_before, self.get_sortable_item(elements, timeout)

    def change_order(self, tab_locator, items_locator):
        self.find_is_visible_no_scroll(tab_locator).click()
        return self.swap_elements(items_locator)

    def change_list_order(self):
        return self.change_order(self.locators.TAB_LIST, self.locators.LIST_ITEM)

    def change_grid_order(self):
        return self.change_order(self.locators.TAB_GRID, self.locators.GRID_ITEM)
