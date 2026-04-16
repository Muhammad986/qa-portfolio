import random
import time

import allure
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.common.exceptions import MoveTargetOutOfBoundsException


from pages.base_page import BasePage
from locators.interactions_page_locators import DraggablePageLocators, DroppablePageLocators, ResizablePageLocators, SelectablePageLocators, SortablePageLocators


class SortablePage(BasePage):
    locators = SortablePageLocators()

    @allure.step('Get sortable items text')
    def get_sortable_item(self, elements, timeout=5):
        def visible_items(driver):
            items = [item for item in driver.find_elements(*elements) if item.is_displayed()]
            return items if items else False

        item_list = wait(self.driver, timeout).until(visible_items)
        return [item.text.strip() for item in item_list]

    @allure.step('Get sortable item element by text')
    def get_sortable_item_element(self, elements, text, timeout=5):
        def visible_item_by_text(driver):
            for item in driver.find_elements(*elements):
                if item.is_displayed() and item.text.strip() == text:
                    return item
            return False

        return wait(self.driver, timeout).until(visible_item_by_text)

    @allure.step('Wait for new order of sortable items')
    def wait_for_new_order(self, elements, order_before, timeout=5):
        def order_changed(driver):
            current_order = self.get_sortable_item(elements, timeout)
            return current_order if current_order != order_before else False

        return wait(self.driver, timeout).until(order_changed)

    @allure.step('Swap two sortable items')
    def swap_elements(self, elements, timeout=5, attempts=3):
        order_before = self.get_sortable_item(elements, timeout)
        with allure.step(f'Original order: {order_before}'):
            source_index = random.randint(1, len(order_before) - 1)

        source_text = order_before[source_index]
        target_text = order_before[source_index - 1]

        for _ in range(attempts):
            with allure.step('Get sortable item elements by text'):
                item_what = self.get_sortable_item_element(elements, source_text, timeout)
                item_where = self.get_sortable_item_element(elements, target_text, timeout)

            with allure.step(f'Drag "{source_text}" and drop on "{target_text}"'):
                self.action_drag_and_drop_to_element(item_what, item_where)

            try:
                order_after = self.wait_for_new_order(elements, order_before, timeout)
                return order_before, order_after
            except TimeoutException:
                continue

        return order_before, self.get_sortable_item(elements, timeout)

    @allure.step('Change order of sortable items')
    def change_order(self, tab_locator, items_locator):
        self.find_is_visible_no_scroll(tab_locator).click()
        return self.swap_elements(items_locator)

    @allure.step('Change order of sortable list')
    def change_list_order(self):
        return self.change_order(self.locators.TAB_LIST, self.locators.LIST_ITEM)

    @allure.step('Change order of sortable grid')
    def change_grid_order(self):
        return self.change_order(self.locators.TAB_GRID, self.locators.GRID_ITEM)

class SelectablePage(BasePage):
    locators = SelectablePageLocators()

    @allure.step('Click on selectable items')
    def click_selectable_item(self, elements):
        item_list = self.find_are_visible(elements)
        if len(item_list) >= 1:
            for item in random.sample(item_list, k=(random.randint(1, len(item_list)))):
                item.click()

    @allure.step('Select active items in selectable list or grid')
    def select_active_item(self, tab_locator, items_locator, active_items_locator):
        self.find_is_visible_no_scroll(tab_locator).click()
        self.click_selectable_item(items_locator)
        active_elements = self.find_are_visible(active_items_locator)
        return [el.text for el in active_elements]

    @allure.step('Select active items in selectable list')
    def select_list_item(self):
        return self.select_active_item(self.locators.TAB_LIST, self.locators.LIST_ITEM, self.locators.LIST_ITEM_ACTIVE)
    
    @allure.step('Select active items in selectable grid')
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
    
    @allure.step('Change size of resizable box')
    def change_size_resizable_box(self):
        with allure.step('action_drag_and_drop to resizable box'):
            self.action_drag_and_drop(self.find_is_present(self.locators.RESIZABLE_BOX_HANDLE), 400, 200)
        with allure.step('Get max size of resizable box'):
            max_size = self.get_px_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        with allure.step('action_drag_and_drop to resizable box'):
            self.action_drag_and_drop(self.find_is_present(self.locators.RESIZABLE_BOX_HANDLE), -400, -300)
        with allure.step('Get min size of resizable box'):
            min_size = self.get_px_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))

        return max_size, min_size

    @allure.step('Change size of resizable element')
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

    @allure.step('Open droppable tab')
    def open_tab(self, tab_locator):
        self.find_is_visible(tab_locator).click()

    @allure.step('Get text of element')
    def get_text(self, locator, timeout=5):
        return self.find_is_visible_no_scroll(locator, timeout).text.strip()

    @allure.step('Wait for specific text to appear in element')
    def wait_for_text(self, locator, expected_text, timeout=5):
        wait(self.driver, timeout).until(
            lambda driver: driver.find_element(*locator).text.strip() == expected_text
        )
        return self.get_text(locator, timeout)

    @allure.step('Perform drag and drop action')
    def drag_to(self, drag_locator, drop_locator, timeout=5):
        drag_element = self.find_is_visible_no_scroll(drag_locator, timeout)
        drop_element = self.find_is_visible_no_scroll(drop_locator, timeout)
        self.action_drag_and_drop_to_element(drag_element, drop_element)

    @allure.step('Drag and drop element and wait for expected text')
    def drag_and_wait_text(self, drag_locator, drop_locator, result_locator, expected_text='Dropped!', timeout=5, attempts=3):
        for _ in range(attempts):
            self.drag_to(drag_locator, drop_locator, timeout)
            try:
                return self.wait_for_text(result_locator, expected_text, timeout)
            except TimeoutException:
                continue
        return self.get_text(result_locator, timeout)

    @allure.step('Get element position')
    def get_position(self, locator, timeout=5):
        element = self.find_is_visible_no_scroll(locator, timeout)
        location = element.location
        return location["x"], location["y"]

    @allure.step('Drag element and get positions before and after move')
    def drag_and_get_positions(self, drag_locator, drop_locator, timeout=5):
        position_before = self.get_position(drag_locator, timeout)
        self.drag_to(drag_locator, drop_locator, timeout)
        position_after_move = self.get_position(drag_locator, timeout)
        return position_before, position_after_move

    @allure.step('Wait until element reverts to original position')
    def wait_until_reverted(self, locator, start_position, timeout=5):
        wait(self.driver, timeout).until(
            lambda driver: self.get_position(locator, timeout) == start_position
        )
        return self.get_position(locator, timeout)

    @allure.step('Check simple droppable scenario')
    def drop_simple(self):
        self.open_tab(self.locators.SIMPLE_TAB)
        return self.drag_and_wait_text(
            self.locators.DRAG_ME_SIMPLE,
            self.locators.DROP_HERE_SIMPLE,
            self.locators.DROP_HERE_SIMPLE
        )

    @allure.step('Check accept and not accept droppable elements')
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

    @allure.step('Check prevent propagation droppable elements')
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

    @allure.step('Drop revert draggable')
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

class DraggablePage(BasePage):
    locators = DraggablePageLocators()

    @allure.step('Get element position')
    def get_position(self, locator, timeout=5):
        element = self.find_is_visible(locator, timeout)
        location = element.location
        return location["x"], location["y"]

    @allure.step('Wait until element position changes')
    def wait_until_position_changed(self, locator, old_position, timeout=5):
        def position_changed(driver):
            element = driver.find_element(*locator)
            new_position = (element.location["x"], element.location["y"])
            return new_position if new_position != old_position else False

        return wait(self.driver, timeout).until(position_changed)

    @allure.step('Get random offset for drag action')
    def get_random_offset(self, drag_element, container_locator=None):
        if container_locator:
            container = self.find_is_visible(container_locator)
            drag_size = drag_element.size
            drag_location = drag_element.location
            container_size = container.size
            container_location = container.location

            current_x = drag_location["x"] - container_location["x"]
            current_y = drag_location["y"] - container_location["y"]

            min_x = max(-current_x, -100)
            max_x = min(container_size["width"] - drag_size["width"] - current_x, 100)
            min_y = max(-current_y, -100)
            max_y = min(container_size["height"] - drag_size["height"] - current_y, 100)
        else:
            viewport_width = self.driver.execute_script("return window.innerWidth")
            viewport_height = self.driver.execute_script("return window.innerHeight")

            rect = self.driver.execute_script("""
                const r = arguments[0].getBoundingClientRect();
                return {
                    left: r.left,
                    top: r.top,
                    width: r.width,
                    height: r.height
                };
            """, drag_element)

            center_x = rect["left"] + rect["width"] / 2
            center_y = rect["top"] + rect["height"] / 2
            safety = 10

            min_x = max(int(-center_x + safety), -150)
            max_x = min(int(viewport_width - center_x - safety), 150)
            min_y = max(int(-center_y + safety), -150)
            max_y = min(int(viewport_height - center_y - safety), 150)

        while True:
            x_offset = random.randint(min_x, max_x) if min_x != max_x else min_x
            y_offset = random.randint(min_y, max_y) if min_y != max_y else min_y

            if x_offset != 0 or y_offset != 0:
                return x_offset, y_offset

    @allure.step('Get positions before and after drag action')
    def get_before_and_after_position(self, drag_locator, container_locator=None, timeout=5):
        for _ in range(3):
            drag_element = self.find_is_visible(drag_locator, timeout)
            before_position = self.get_position(drag_locator, timeout)

            x_offset, y_offset = self.get_random_offset(drag_element, container_locator)

            try:
                self.action_drag_and_drop(drag_element, x_offset, y_offset)
                after_position = self.wait_until_position_changed(drag_locator, before_position, timeout)
                return before_position, after_position
            except (TimeoutException, MoveTargetOutOfBoundsException):
                continue

        return before_position, self.get_position(drag_locator, timeout)

    @allure.step('Check simple draggable scenario')
    def simple_drag_box(self):
        self.find_is_visible(self.locators.SIMPLE_TAB).click()
        return self.get_before_and_after_position(self.locators.DRAG_ME)

    @allure.step('Check axis restricted draggable scenario')
    def axis_restricted_box(self, loc):
        loc_X_and_Y = {
            'x': self.locators.ONLY_X,
            'y': self.locators.ONLY_Y
        }
        self.find_is_visible(self.locators.AXIC_RESTRICTED_TAB).click()
        if loc == 'x':
            before, after = self.get_before_and_after_position(loc_X_and_Y[loc])
            return before[0], after[0]
        else:
            before, after = self.get_before_and_after_position(loc_X_and_Y[loc])
            return before[1], after[1]
        
    @allure.step('Check container restricted draggable scenario')
    def container_restricted(self, container):
        parent_and_box_locator = {
            'box': {
                'drag': self.locators.BOX_COMPONENT,
                'contain': self.locators.BOX_CONTEINER
            },
            'parent': {
                'drag': self.locators.PARENT_COMPONENT,
                'contain': self.locators.PARENT_CONTAINER
            }
        }
        self.find_is_visible(self.locators.CONTAINER_RESTRICTED_TAB).click()

        return self.get_before_and_after_position(
            parent_and_box_locator[container]['drag'],
            parent_and_box_locator[container]['contain']
        )
