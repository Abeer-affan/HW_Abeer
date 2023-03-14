from selenium.webdriver.common.by import By
import pytest
import time
from pytestProject3.BaseClass import BaseClass
from pytestProject3.conftest import *
import logging as logger


@pytest.mark.usefixtures("setup")
@pytest.mark.Fun
class Testfunc(BaseClass):
    def test_Add_game_func(self, setup): #It is not work , because I didn't have a way to my computer in selenium
        logger = self.getLogger()
        setup.get("http://127.0.0.1:5000/")
        setup.find_element(By.XPATH, "//button[normalize-space()='ADD GAME']").click()
        time.sleep(3)
        setup.find_element(By.XPATH, "//input[@name='filename']").click()
        time.sleep(3)
        setup.find_element(By.XPATH, "//input[@name='filename']").send_keys("PS4 - MORTAL KOMBAT X.jpg")
        time.sleep(3)
        setup.find_element(By.XPATH, "//input[@name='Game_title']").send_keys("PS4 - MORTAL KOMBAT X")
        setup.find_element(By.XPATH, "//textarea[@name='description']").send_keys("A fight game . very interesting game ")
        setup.find_element(By.XPATH, "//input[@name='age']").send_keys("+18")
        setup.find_element(By.XPATH, "//input[@name='price']").send_keys("120")
        setup.find_element(By.XPATH, "//input[@name='online_play']").send_keys("No")
        setup.find_element(By.XPATH, "//input[@name='multiplayer']").send_keys("Yes")
        setup.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
        setup.get_screenshot_as_file("A new game Added")
        assert setup.find_element(By.XPATH, "//button[normalize-space()='Update']").is_displayed()
        logger.info("Add game- test case  - Passed!")


    def test_Add_comment(self, setup):
        logger = self.getLogger()
        setup.get("http://127.0.0.1:5000/")
        setup.find_element(By.XPATH, "//body/a[5]").click()
        time.sleep(2)
        setup.find_element(By.XPATH,"//input[@name='name']").send_keys("Abeer Affan ")
        setup.find_element(By.XPATH,"//textarea[@name='comment_text']").send_keys("It's a nice game ")
        setup.find_element(By.XPATH,"//button[normalize-space()='ADD']").click()
        setup.get_screenshot_as_file("NEW COMMENT ADDED")
        assert setup.find_element(By.XPATH,"//body/a[5]").is_displayed()
        logger.info("You added the comment successfully")

    def test_Delete_game_and_BackToHomePgae(self, setup):
        logger = self.getLogger()
        setup.get("http://127.0.0.1:5000/")
        # Navigate to game page and delete game
        setup.find_element(By.XPATH, "//body/a[12]").click()
        delete_button = setup.find_element(By.XPATH, "//button[normalize-space()='Delete']")
        game_title = setup.find_element(By.XPATH, "//h1").text
        delete_button.click()

        # Verify that game is deleted
        assert game_title not in setup.page_source
        logger.info(" The Game deleted successfully".format(game_title))

    def test_required_argument(self,setup):
        logger = self.getLogger()
        setup.get("http://127.0.0.1:5000/")
        setup.find_element(By.XPATH,"//button[normalize-space()='ADD GAME']").click()
        Arguments=[setup.find_element(By.XPATH,"//input[@name='PRICE(NIS)']").text,
                    setup.find_element(By.XPATH,"//input[@name='Age']").text,
                    setup.find_element(By.XPATH,"//input[@name='GAME TITLE']").text,
                    setup.find_element(By.XPATH,"(//label[normalize-space()='FILENAME'])[1]"),
                   setup.find_element(By.XPATH,"//input[@name='filename']"),
                   setup.find_element(By.XPATH,"//input[@name='online_play']"),
                   setup.find_element(By.XPATH,"//input[@name='multiplayer']")]
        assert  "CHECK THE ELEMENTS THERE ARE AN ERROR"
        if len(Arguments)==7 :
            logger.info("your test is successes")


    def test_AddTwoPictures(self,setup):
        def test_Add_game_func(self, setup):  # It is not work , because I didn't have a way to my computer in selenium
            logger = self.getLogger()
            setup.get("http://127.0.0.1:5000/")
            setup.find_element(By.XPATH, "//button[normalize-space()='ADD GAME']").click()
            time.sleep(3)
            setup.find_element(By.XPATH, "//input[@name='filename']").click()
            time.sleep(3)
            setup.find_element(By.XPATH, "//input[@name='filename']").send_keys("PS4 - MORTAL KOMBAT X.jpg")
            time.sleep(3)
            setup.find_element(By.XPATH, "//input[@name='filename']").send_keys("The Settlers-New Allies.jpg")
            time.sleep(3)
            setup.find_element(By.XPATH, "//input[@name='Game_title']").send_keys("PS4 - MORTAL KOMBAT X")
            setup.find_element(By.XPATH, "//textarea[@name='description']").send_keys(
                "A fight game . very interesting game ")
            setup.find_element(By.XPATH, "//input[@name='age']").send_keys("+18")
            setup.find_element(By.XPATH, "//input[@name='price']").send_keys("120")
            setup.find_element(By.XPATH, "//input[@name='online_play']").send_keys("No")
            setup.find_element(By.XPATH, "//input[@name='multiplayer']").send_keys("Yes")
            setup.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
            setup.get_screenshot_as_file("A new game Added")
            assert setup.find_element(By.XPATH, "//button[normalize-space()='Update']").is_displayed()
            logger.info("Add game with a second image - test case  - Passed!")

    def test_logo(self,setup):
        logger = self.getLogger()
        setup.get("http://127.0.0.1:5000/")
        setup.find_element(By.XPATH, "//body/a[9]").click()
        setup.find_element(By.XPATH, "//a[normalize-space()='']//img").click()
        assert setup.find_element(By.XPATH, "//a[normalize-space()='']//img")
        logger.info(" test case--logo - Passed!")

    def test_support(self,setup):
        logger = self.getLogger()
        setup.get("http://127.0.0.1:5000/")
        setup.find_element(By.XPATH, "//body/a[6]").click()
        setup.find_element(By.XPATH, "//h3[normalize-space()='Support']").click()
        assert setup.find_element(By.XPATH, "//h3[normalize-space()='Support']")
        logger.info(" test case support - Passed!")






