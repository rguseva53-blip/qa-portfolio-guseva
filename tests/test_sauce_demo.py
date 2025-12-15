from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_login_sauce_demo():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 10)

    username = wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    password = driver.find_element(By.ID, "password")
    login_btn = driver.find_element(By.ID, "login-button")

    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_btn.click()

    time.sleep(2)

    assert "inventory" in driver.current_url

    driver.quit()
0

