from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service("D:\Python\Selenium\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()
print(driver.title)
print(driver.current_url)

time.sleep(10)

