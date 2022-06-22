import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, executable_path='C:\\chromedriver.exe')
#Reading The Email And Password fromt the txt file
file = open("D:\\LinkedIn.txt")
lines = file.readlines()
username = lines[0]
password = lines[1]
#getting the target link
driver.get('https://www.linkedin.com/uas/login')
#passing the Email and Password to the target input
ElementId = driver.find_element(by=By.ID, value="username")
ElementId.send_keys(username)
ElementId = driver.find_element(by=By.ID, value="password")
# button = driver.find_elements_by_class_name("btn__primary--large")
# button = [Email, Password]
ElementId.send_keys(password)
ElementId.submit()
#navigating to the target page
try:
    myNetwork = WebDriverWait(driver, 13).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Jobs"))
    )
    myNetwork.click()
    try:
        profiles = WebDriverWait(driver, 13).until(
            EC.presence_of_element_located((By.XPATH, "//section[@class='artdeco-card ember-view mb2 ph3 pt5 pb1 ']"))
        )
        print(profiles.text())
    except:
        print("There is an error parsing the profiles")
except:
    driver.quit()


#visitedProfiles = []
#queuedProfiles = []


