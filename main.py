# https://chromedriver.chromium.org/downloads
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(PATH)
# 巴哈姆特
driver.get("https://user.gamer.com.tw/login.php")
print(driver.title)
username = driver.find_element_by_name("userid")
password = driver.find_element_by_name("password")
username.send_keys("")
password.send_keys("")
password.send_keys(Keys.RETURN)
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "signin-btn"))
)
signInBtn = driver.find_element_by_id("signin-btn")
if "每日簽到已達成" in signInBtn.text:
    print("已簽到")
else:
    signInBtn.click()
    print("簽到完成")
driver.quit()
