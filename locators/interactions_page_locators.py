
from selenium.webdriver.common.by import By

class SortablePageLocators:
    TAB_LIST = (By.CSS_SELECTOR, 'button[id="demo-tab-list"]')
    LIST_ITEM = (By.CSS_SELECTOR, 'div.list-group div.list-group-item')
    TAB_GRID = (By.CSS_SELECTOR, 'button[id="demo-tab-grid"]')
    GRID_ITEM = (By.CSS_SELECTOR, 'div.create-grid div.list-group-item')

class SelectablePageLocators:
    TAB_LIST = (By.CSS_SELECTOR, 'button[id="demo-tab-list"]')
    LIST_ITEM = (By.CSS_SELECTOR, 'li[class="mt-2 list-group-item list-group-item-action"]')
    LIST_ITEM_ACTIVE = (By.CSS_SELECTOR, 'li[class="mt-2 list-group-item active list-group-item-action"]')
    TAB_GRID = (By.CSS_SELECTOR, 'button[id="demo-tab-grid"]')
    GRID_ITEM = (By.CSS_SELECTOR, 'li[class="list-group-item list-group-item-action"]')
    GRID_ITEM_ACTIVE = (By.CSS_SELECTOR, 'li[class="list-group-item active list-group-item-action"]')

class ResizablePageLocators:
    RESIZABLE_BOX_HANDLE = (By.CSS_SELECTOR, 'div[class="constraint-area"] span[class="react-resizable-handle react-resizable-handle-se"]')
    RESIZABLE_BOX = (By.CSS_SELECTOR, 'div[id="resizableBoxWithRestriction"]')
    RESIZABLE_HANDLE = (By.CSS_SELECTOR, 'div[id="resizable"] span[class="react-resizable-handle react-resizable-handle-se"]')
    RESIZABLE = (By.CSS_SELECTOR, 'div[id="resizable"]')

class DroppablePageLocators:
    # Simple
    SIMPLE_TAB = (By.CSS_SELECTOR, 'button[id="droppableExample-tab-simple"]')
    DRAG_ME_SIMPLE = (By.CSS_SELECTOR, 'div[id="draggable"]')
    DROP_HERE_SIMPLE = (By.CSS_SELECTOR, '#simpleDropContainer #droppable')

    # Accept
    ACCEPT_TAB = (By.CSS_SELECTOR, 'button[id="droppableExample-tab-accept"]')
    ACCEPTABLE = (By.CSS_SELECTOR, 'div[id="acceptable"]')
    NOT_ACCEPTABLE = (By.XPATH, '//*[@id="acceptDropContainer"]//div[contains(@class, "ui-draggable")][2]')
    DROP_HERE_ACCEPT = (By.CSS_SELECTOR, '#acceptDropContainer div.ui-droppable')

    # Prevent Propogation
    PREVENT_TAB = (By.CSS_SELECTOR, 'button[id="droppableExample-tab-preventPropogation"]')
    NOT_GREEDY_DROP_BOX_TEXT = (By.XPATH, '//div[@id="notGreedyDropBox"]/p')
    NOT_GREEDY_INNER_BOX = (By.CSS_SELECTOR, 'div[id="notGreedyInnerDropBox"]')
    GREEDY_DROP_BOX_TEXT = (By.XPATH, '//div[@id="greedyDropBox"]/p')
    GREEDY_INNER_BOX = (By.CSS_SELECTOR, 'div[id="greedyDropBoxInner"]')
    DRAG_ME_PREVENT = (By.CSS_SELECTOR, '#ppDropContainer #dragBox')

    # Revert Draggable
    REVERT_TAB = (By.CSS_SELECTOR, 'button[id="droppableExample-tab-revertable"]')
    WILL_REVERT = (By.CSS_SELECTOR, 'div[id="revertable"]')
    NOT_REVERT = (By.CSS_SELECTOR, 'div[id="notRevertable"]')
    DROP_HERE_REVERT = (By.CSS_SELECTOR, '#revertableDropContainer #droppable')

class DraggablePageLocators:
    #Simple
    SIMPLE_TAB = (By.CSS_SELECTOR, 'button[id="draggableExample-tab-simple"]')
    DRAG_ME = (By.CSS_SELECTOR, '#draggableExample-tabpane-simple #dragBox')
    SIMPLE_CONTAINER = (By.CSS_SELECTOR, 'div[class="dragable-container"]')

    #Axic Restricted
    AXIC_RESTRICTED_TAB = (By.CSS_SELECTOR, 'button[id="draggableExample-tab-axisRestriction"]')
    ONLY_X = (By.CSS_SELECTOR, 'div[id="restrictedX"]')
    ONLY_Y = (By.CSS_SELECTOR, 'div[id="restrictedY"]')

    #Container Restricted
    CONTAINER_RESTRICTED_TAB = (By.CSS_SELECTOR, 'button[id="draggableExample-tab-containerRestriction"]')
    BOX_COMPONENT = (By.CSS_SELECTOR, 'div[id="containmentWrapper"] div.draggable')
    BOX_CONTEINER = (By.CSS_SELECTOR, 'div[id="containmentWrapper"]')
    PARENT_COMPONENT = (By.CSS_SELECTOR, 'div[class="draggable ui-widget-content m-3"] span')
    PARENT_CONTAINER = (By.CSS_SELECTOR, 'div[class="draggable ui-widget-content m-3"]')