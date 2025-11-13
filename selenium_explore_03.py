from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()

name = driver.find_element(By.ID,"name")
name.send_keys('hello')
alertbtn = driver.find_element(By.ID,"alertbtn")
alertbtn.click()

confirmbtn = driver.find_element(By.ID,"confirmbtn")
btntext=confirmbtn.text
print(btntext)



input("Press Enter to close browser...")