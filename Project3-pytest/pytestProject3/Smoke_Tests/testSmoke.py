from selenium.webdriver.common.by import By
import pytest
import time
from pytestProject3.BaseClass import BaseClass
from pytestProject3.conftest import *
import logging as logger

@pytest.mark.usefixtures("setup")
@pytest.mark.acceptance
class TestSmoke(BaseClass):
    def test_add_Comment(self,setup):
        loggerr = self.getLogger()
        setup.get("http://127.0.0.1:5000/")
        setup.find_element(By.XPATH, "//body/a[7]").click()
        time.sleep(2)
        assert setup.find_element(By.XPATH,"//button[normalize-space()='ADD']") .is_displayed()
        loggerr.info("Pass: The Add comment button of the website is displayed ")

    def test_title(self,setup):
        logger= self.getLogger()
        setup.get("http://127.0.0.1:5000/")
        expected_title = "World of PS: Most common games"
        actual_title = setup.find_element(By.XPATH,"//h1[normalize-space()='World of PS: Most common games']").text
        assert expected_title == actual_title
        logger.info("Pass: The title of the website is displayed correctly in the browser tab or window title bar.")

    def test_URL(self,setup):
        logger = self.getLogger()
        setup.get("http://127.0.0.1:5000/")
        actual_URL=setup.current_url
        expceptedUrl="http://127.0.0.1:5000/"
        assert actual_URL ==expceptedUrl ,"Your URL is not correct"
        logger.info("YOUR TEST IS PASSED , YOU IN THE CORRECT URL")
