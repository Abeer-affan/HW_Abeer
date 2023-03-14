from selenium.webdriver.common.by import By
import pytest
import time
from pytestProject3.BaseClass import BaseClass
from pytestProject3.conftest import *
import logging as logger

@pytest.mark.usefixtures("setup")
@pytest.mark.functions
class TestAccept(BaseClass):

    def test_update_game_from_home_page(self, setup):
        logger = self.getLogger()
        setup.get("http://127.0.0.1:5000/")
        setup.find_element(By.XPATH, "//body/a[3]").click()
        setup.find_element(By.XPATH , "//button[normalize-space()='Update']").click()
        time.sleep(5)
        setup.find_element(By.CSS_SELECTOR, "input[name='Game_title']").send_keys("A NEW GAME OF SPIDER MANNNN ")
        time.sleep(5)
        setup.find_element(By.XPATH, "//button[normalize-space()='Update']").click()
        time.sleep(5)
        setup.get_screenshot_as_file('Project3-pytest/pytestProject3/screenshots/acceptance/UpdateGame.jpg')
        assert setup.find_element(By.XPATH, "//button[normalize-space()='Update']").is_displayed()
        logger.info("Acceptance test case 1 - Passed!")


