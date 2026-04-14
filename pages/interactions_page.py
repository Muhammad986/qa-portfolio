import random
import time

from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait as wait

from pages.base_page import BasePage
from locators.interactions_page_locators import DroppablePageLocators, ResizablePageLocators, SelectablePageLocators, SortablePageLocators


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

class SelectablePage(BasePage):
    locators = SelectablePageLocators()

    def click_selectable_item(self, elements):
        item_list = self.find_are_visible(elements)
        if len(item_list) >= 1:
            for item in random.sample(item_list, k=(random.randint(1, len(item_list)))):
                item.click()

    def select_active_item(self, tab_locator, items_locator, active_items_locator):
        self.find_is_visible_no_scroll(tab_locator).click()
        self.click_selectable_item(items_locator)
        active_elements = self.find_are_visible(active_items_locator)
        return [el.text for el in active_elements]

    def select_list_item(self):
        return self.select_active_item(self.locators.TAB_LIST, self.locators.LIST_ITEM, self.locators.LIST_ITEM_ACTIVE)
    
    def select_grid_item(self):
        return self.select_active_item(self.locators.TAB_GRID, self.locators.GRID_ITEM, self.locators.GRID_ITEM_ACTIVE)
    
class ResizablePage(BasePage):
    locators = ResizablePageLocators()

    def get_px_width_height(self, value_of_size):
        width = value_of_size.split(';')[0].split(':')[1].replace(' ', '')
        height = value_of_size.split(';')[1].split(':')[1].replace(' ', '')
        return width, height
    
    def get_max_min_size(self, element):
        size = self.find_is_present(element)
        size_value = size.get_attribute('style')
        return size_value
    
    def change_size_resizable_box(self):
        self.action_drag_and_drop(self.find_is_present(self.locators.RESIZABLE_BOX_HANDLE), 400, 200)
        max_size = self.get_px_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        self.action_drag_and_drop(self.find_is_present(self.locators.RESIZABLE_BOX_HANDLE), -400, -300)
        min_size = self.get_px_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))

        return max_size, min_size


    def change_size_resizable(self):
        self.scroll_to_page_bottom()

        handle = self.find_is_present(self.locators.RESIZABLE_HANDLE)
        self.action_drag_and_drop(handle, random.randint(1, 100), random.randint(1, 100))
        max_size = self.get_px_width_height(self.get_max_min_size(self.locators.RESIZABLE))

        self.action_drag_and_drop(handle, random.randint(-100, -1), random.randint(-100, -1))
        min_size = self.get_px_width_height(self.get_max_min_size(self.locators.RESIZABLE))

        return max_size, min_size
    
class DroppablePage(BasePage):
    locators = DroppablePageLocators()

    def open_tab(self, tab_locator):
        self.find_is_visible(tab_locator).click()

    def get_text(self, locator, timeout=5):
        return self.find_is_visible_no_scroll(locator, timeout).text.strip()

    def wait_for_text(self, locator, expected_text, timeout=5):
        wait(self.driver, timeout).until(
            lambda driver: driver.find_element(*locator).text.strip() == expected_text
        )
        return self.get_text(locator, timeout)

    def drag_to(self, drag_locator, drop_locator, timeout=5):
        drag_element = self.find_is_visible_no_scroll(drag_locator, timeout)
        drop_element = self.find_is_visible_no_scroll(drop_locator, timeout)
        self.action_drag_and_drop_to_element(drag_element, drop_element)

    def drag_and_wait_text(self, drag_locator, drop_locator, result_locator, expected_text='Dropped!', timeout=5, attempts=3):
        for _ in range(attempts):
            self.drag_to(drag_locator, drop_locator, timeout)
            try:
                return self.wait_for_text(result_locator, expected_text, timeout)
            except TimeoutException:
                continue
        return self.get_text(result_locator, timeout)

    def get_position(self, locator, timeout=5):
        element = self.find_is_visible_no_scroll(locator, timeout)
        location = element.location
        return location["x"], location["y"]

    def drag_and_get_positions(self, drag_locator, drop_locator, timeout=5):
        position_before = self.get_position(drag_locator, timeout)
        self.drag_to(drag_locator, drop_locator, timeout)
        position_after_move = self.get_position(drag_locator, timeout)
        return position_before, position_after_move

    def wait_until_reverted(self, locator, start_position, timeout=5):
        wait(self.driver, timeout).until(
            lambda driver: self.get_position(locator, timeout) == start_position
        )
        return self.get_position(locator, timeout)

    def drop_simple(self):
        self.open_tab(self.locators.SIMPLE_TAB)
        return self.drag_and_wait_text(
            self.locators.DRAG_ME_SIMPLE,
            self.locators.DROP_HERE_SIMPLE,
            self.locators.DROP_HERE_SIMPLE
        )

    def drop_accept(self):
        self.open_tab(self.locators.ACCEPT_TAB)

        self.drag_to(self.locators.NOT_ACCEPTABLE, self.locators.DROP_HERE_ACCEPT)
        result_no_accept = self.get_text(self.locators.DROP_HERE_ACCEPT)

        result_accept = self.drag_and_wait_text(
            self.locators.ACCEPTABLE,
            self.locators.DROP_HERE_ACCEPT,
            self.locators.DROP_HERE_ACCEPT
        )

        return result_no_accept, result_accept

    def drop_prevent_propogation(self):
        self.open_tab(self.locators.PREVENT_TAB)

        text_not_greedy_inner_box = self.drag_and_wait_text(
            self.locators.DRAG_ME_PREVENT,
            self.locators.NOT_GREEDY_INNER_BOX,
            self.locators.NOT_GREEDY_INNER_BOX
        )
        text_not_greedy_box = self.wait_for_text(
            self.locators.NOT_GREEDY_DROP_BOX_TEXT,
            'Dropped!'
        )

        text_greedy_inner_box = self.drag_and_wait_text(
            self.locators.DRAG_ME_PREVENT,
            self.locators.GREEDY_INNER_BOX,
            self.locators.GREEDY_INNER_BOX
        )
        text_greedy_drop_box = self.get_text(self.locators.GREEDY_DROP_BOX_TEXT)

        return (
            text_not_greedy_box,
            text_not_greedy_inner_box,
            text_greedy_drop_box,
            text_greedy_inner_box
        )

    def drop_revert_draggable(self, type_drag, timeout=5):
        drags = {
            'will': self.locators.WILL_REVERT,
            'not_will': self.locators.NOT_REVERT
        }

        self.open_tab(self.locators.REVERT_TAB)

        drag_locator = drags[type_drag]
        drop_locator = self.locators.DROP_HERE_REVERT

        position_before, position_after_move = self.drag_and_get_positions(
            drag_locator,
            drop_locator,
            timeout
        )

        if type_drag == 'will':
            position_after_revert = self.wait_until_reverted(
                drag_locator,
                position_before,
                timeout
            )
        else:
            position_after_revert = self.get_position(drag_locator, timeout)

        return position_after_move, position_after_revert
