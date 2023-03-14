from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import logging
import inspect
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import logging
@pytest.fixture(params=["chrome", "edge"])
def setup(request):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    if request.param == "chrome":
        service_obj = Service("chromedriver_win32/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj, options=chrome_options)
    elif request.param == "edge":
        driver = webdriver.Edge("msedgedriver.exe")
    else:
        driver = None
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    if driver:
        driver.quit()

def logging():
    logger = logging.getLogger(__name__)
    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    logger.setLevel(logging.DEBUG)
    logger.info("This is some log line")
    logger.warning("A warning")
    logger.debug("A debug")
        # DEBUG
        # INFO
        # WARNING
        # ERROR
        # CRITICAL