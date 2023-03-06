import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Create a Service object for the Chrome browser
service_obj = Service("Chrome Browser/chromedriver_win32/chromedriver.exe")

# Use the Service object to instantiate a Chrome driver object
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(3)
# Maximize the window
driver.maximize_window()
driver.get("http://127.0.0.1:5000/")
##Test1
driver.find_element(By.XPATH,"//body/a[3]").click()
driver.find_element(By.XPATH,"//body/a[3]").click()
driver.find_element(By.XPATH,"//input[@name='Game_title']").send_keys("A NEW GAME OF SPIDER MAN ")
driver.find_element(By.XPATH,"//button[normalize-space()='Update']").click()
##Test2
driver.find_element(By.XPATH,"//a[normalize-space()='']//img").click() #back to home page
driver.find_element(By.XPATH,"//body/a[5]").click()
driver.find_element(By.XPATH,"//button[normalize-space()='Update']").click()
#Test3
driver.find_element(By.XPATH,"//a[normalize-space()='']//img").click() #back to home page
driver.find_element(By.XPATH,"//button[normalize-space()='ADD GAME']").click()
driver.find_element(By.XPATH,"//input[@name='filename']").send_keys("C:/Users/DELL/Desktop/PS4 - MORTAL KOMBAT X")
driver.find_element(By.XPATH,"//input[@name='Game_title']").send_keys("PS4 - MORTAL KOMBAT X")
driver.find_element(By.XPATH,"//textarea[@name='description']").send_keys("A fight game . very interesting game ")
driver.find_element(By.XPATH,"//input[@name='age']").send_keys("+18")
driver.find_element(By.XPATH,"//input[@name='price']").send_keys("120")
driver.find_element(By.XPATH,"//input[@name='online_play']").send_keys("No")
driver.find_element(By.XPATH,"//input[@name='multiplayer']").send_keys("Yes")
driver.find_element(By.XPATH,"//button[normalize-space()='Add']").click()
# ##Test 4
driver.find_element(By.XPATH,"//a[normalize-space()='']//img").click() #back to home page
driver.find_element(By.XPATH,"//body/a[12]").click()
driver.find_element(By.XPATH,"//button[normalize-space()='Delete']").click()

##Test5
driver.find_element(By.XPATH,"//a[normalize-space()='']//img").click() #back to home page

##Test6
driver.find_element(By.XPATH,"//body/a[10]").click()
driver.find_element(By.XPATH,"//i[@class='bx bxl-facebook']").click()
##Test7
driver.find_element(By.XPATH,"//a[normalize-space()='']//img").click() #back to home page
driver.find_element(By.XPATH,"//body/a[9]").click()
driver.find_element(By.XPATH,"//input[@name='name']").send_keys("Abeer Affan ")
driver.find_element(By.XPATH,"//textarea[@name='comment_text']").send_keys("It is a wonderful game ")
driver.find_element(By.XPATH,"//button[normalize-space()='ADD']").click()
##Test 8
driver.find_element(By.XPATH,"//a[normalize-space()='']//img").click() #back to home page
driver.find_element(By.XPATH,"//body/a[9]").click()
driver.find_element(By.XPATH,"//input[@name='name']").send_keys("Abeer Affan ")
driver.find_element(By.XPATH,"//textarea[@name='comment_text']").send_keys("It is a bad  game ")
driver.find_element(By.XPATH,"//button[normalize-space()='ADD']").click()
##Test9
driver.find_element(By.XPATH,"//a[normalize-space()='']//img").click() #back to home page
driver.find_element(By.XPATH,"//body/a[6]").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Product']").click()

#Test 10
driver.find_element(By.XPATH,"//a[normalize-space()='']//img").click() #back to home page
driver.find_element(By.XPATH,"//button[normalize-space()='ADD GAME']").click()
driver.find_element(By.XPATH,"//input[@name='filename']").send_keys("C:/Users/DELL/Desktop/PS4 - MORTAL KOMBAT X")
driver.find_element(By.XPATH,"//input[@name='Game_title']").send_keys("PS4 - MORTAL KOMBAT X")
driver.find_element(By.XPATH,"//textarea[@name='description']").send_keys("A fight game . very interesting game ")
driver.find_element(By.XPATH,"//input[@name='age']").send_keys("+18")
driver.find_element(By.XPATH,"//input[@name='price']").send_keys("120")
driver.find_element(By.XPATH,"//input[@name='multiplayer']").send_keys("Yes")
driver.find_element(By.XPATH,"//button[normalize-space()='Add']").click()