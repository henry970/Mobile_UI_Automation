from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Mobile_Automation_test.LoginPageLocators.Login_page_locators_test import LoginPageLocators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def click_sign(self):
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.SIGN_BUTTON)
        )
        login_button.click()

    def enter_username(self, username):
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.USERNAME_FIELD)
        )
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.PASSWORD_FIELD)
        )
        password_field.send_keys(password)

    def click_login(self):
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
        )
        login_button.click()
