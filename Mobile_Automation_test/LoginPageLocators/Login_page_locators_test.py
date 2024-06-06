from selenium.webdriver.common.by import By


class LoginPageLocators:
    SIGN_BUTTON = (By.XPATH, '//*[@id="selectedElementContainer"]/div/div[2]/div/div['
                             '2]/div/div/div/div/div/table/tbody/tr/td[2]')

    USERNAME_FIELD = (By.ID, 'com.example.myapp:id/username')
    PASSWORD_FIELD = (By.ID, 'com.example.myapp:id/password')
    LOGIN_BUTTON = (By.ID, 'com.example.myapp:id/login')
    WELCOME_MESSAGE = (By.ID, 'com.example.myapp:id/welcome')
