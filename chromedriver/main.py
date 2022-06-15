import time
from selenium import webdriver

url = "https://www.instagram.com/"
driver = webdriver.Chrome(executable_path="/home/dmitriy/Projects/QA/chromedriver/chromedriver")

try:
    driver.get(url=url)
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close
    driver.quit