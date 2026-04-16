from datetime import datetime
import os
import allure
import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    download_dir = os.path.abspath("file_for_tests")

    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
    })

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f"screenshot {datetime.today()}", attachment_type=allure.attachment_type.PNG)
    driver.quit()
