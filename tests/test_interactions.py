

import time

from pages.interactions_page import DraggablePage, DroppablePage, ResizablePage, SelectablePage, SortablePage


class TestInteractions:
    class TestSortablePage:
        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            list_before, list_after = sortable_page.change_list_order()
            grid_before, grid_after = sortable_page.change_grid_order()
            assert list_before != list_after, 'The order of the list has not been changed.'
            assert grid_before != grid_after, 'The order of the grid has not changed.'

    class TestSelectablePage:
        def test_selectable_page(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            item_list = selectable_page.select_list_item()
            item_grid = selectable_page.select_grid_item()
            assert len(item_list) > 0, 'No elements were selected'
            assert len(item_grid) > 0, 'No elements were selected'

    class TestResizable:
        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            max_box, min_box = resizable_page.change_size_resizable_box()
            max_resizable, min_resizable = resizable_page.change_size_resizable()

            assert ('500px', '300px') == max_box, "Maximum size not equal to '500px', '300px'"
            assert ('150px', '150px') == min_box, "Minimum size not equal to '150px', '150px'"
            assert max_resizable != min_resizable, "Resizable has not been changed"

    class TestDroppable:
        def test_simple_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            text = droppable_page.drop_simple()
            assert text == 'Dropped!', 'The elements has not been dropped.'

        def test_accert_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            result_no_accept, result_accept = droppable_page.drop_accept()
            assert result_no_accept == 'Drop here', "The dropped element has been accepted."
            assert result_accept == 'Dropped!', 'The dropped element has not been accepted.'

        def test_prevent_propogation_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            not_greedy, not_greedy_inner, greedy, greedy_inner = droppable_page.drop_prevent_propogation()
            assert not_greedy == 'Dropped!', 'The elements texts has not been changed.'
            assert not_greedy_inner == 'Dropped!', 'The elements texts has not been changed.'
            assert greedy == 'Outer droppable', 'The elements texts has been changed.'
            assert greedy_inner == 'Dropped!', 'The elements texts has not been changed.'

        def test_revert_draggable_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            will_after_move, will_after_revert = droppable_page.drop_revert_draggable('will')
            not_will_after_move, not_will_after_revert = droppable_page.drop_revert_draggable('not_will')

            assert will_after_move != will_after_revert, 'The element has not reverted'
            assert not_will_after_move == not_will_after_revert, 'The element has reverted'
    
    class TestDraggable:
        def test_simple_draggable(self, driver):
            dragabble_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
            dragabble_page.open()
            before, after = dragabble_page.simple_drag_box()
            print(before)
            print(after)
            assert before != after, 'The position of the box has not been changed.'

        def test_axis_restricted_draggable(self, driver):
            dragabble_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
            dragabble_page.open()
            before_x, after_x = dragabble_page.axis_restricted_box('x')
            before_y, after_y = dragabble_page.axis_restricted_box('y')
            assert before_x != after_x, 'The position of the box has not been changed.'
            assert before_y != after_y, 'The position of the box has not been changed.'

        def test_container_restricred_draggable(self, driver):
            dragabble_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
            dragabble_page.open()
            before_box, after_box = dragabble_page.container_restricted('box')
            before_parent, after_parent = dragabble_page.container_restricted('parent')
            assert before_box != after_box, 'The position of the box has not been changed.'
            assert before_parent != after_parent, 'The position of the box has not been changed.'