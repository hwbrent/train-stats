import os

from selenium.webdriver.common.by import By

from chromedriver_utils.init import init


PARENT_DIR = os.path.dirname(__file__)
PY_ROOT = os.path.join(PARENT_DIR, os.pardir)
CHROMEDRIVER_PATH = os.path.join(PY_ROOT, "chromedriver")


LOGIN_PAGE_URL = "https://www.thetrainline.com/en-us/my-account/login"


def login():
    # Get webdriver
    driver = init(CHROMEDRIVER_PATH)

    # Navigate to login page
    driver.get(LOGIN_PAGE_URL)

    # Get rid of the cookies dialog
    accept_cookies_button = driver.find_element(By.ID, "onetrust-accept-btn-handler")
    accept_cookies_button.click()

    # Find email field and fill it in
    email_input = driver.find_element(By.ID, "signin-email")
    email_input.send_keys()

    # Find password field and fill it in
    password_input = driver.find_element(By.ID, "signin-password")
    password_input.send_keys()

    # Find submit button and click it
    signin_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    signin_button.click()


if __name__ == "__main__":
    login()
