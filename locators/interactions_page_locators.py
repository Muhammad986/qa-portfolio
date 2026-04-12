
from selenium.webdriver.common.by import By

class SortablePageLocators():
    TAB_LIST = (By.CSS_SELECTOR, 'button[id="demo-tab-list"]')
    LIST_ITEM = (By.CSS_SELECTOR, 'div.list-group div.list-group-item')
    TAB_GRID = (By.CSS_SELECTOR, 'button[id="demo-tab-grid"]')
    GRID_ITEM = (By.CSS_SELECTOR, 'div.create-grid div.list-group-item')