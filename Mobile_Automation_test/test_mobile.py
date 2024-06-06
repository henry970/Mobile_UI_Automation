import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from Mobile_Automation_test.loginPage.login_page_test import LoginPage


@pytest.fixture(scope='module')
def driver():
    # Create an instance of UiAutomator2Options and set desired capabilities
    options = UiAutomator2Options()
    options.platformName = 'Android'
    options.deviceName = "Henry'sA23"
    options.platformVersion = '14.0'
    options.orientation = 'PORTRAIT'
    options.automationName = 'UiAutomator2'
    options.appWaitActivity = 'com.wdiodemoapp.MainActivity'
    options.newCommandTimeout = 240
    options.connectHardwareKeyboard = True

    # Convert options to capabilities
    capabilities = options.to_capabilities()

    # Initialize the Appium driver with the specified capabilities
    driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)

    # Debug prints
    print("Options: ", options)
    print("Capabilities: ", capabilities)

    yield driver

    # Quit the driver after tests are done
    driver.quit()


def test_login(driver):
    login_page = LoginPage(driver)
    login_page.click_sign()

# import pytest
# from appium import webdriver
#
# from Mobile_Automation_test.loginPage.login_page_test import LoginPage

# @pytest.fixture(scope='module')
# def driver():
#     desired_caps = {
#         "platformName": "Android",
#         "maxInstances": 1,
#         "deviceName": "Henry'sA23",
#         "platformVersion": "14.0",
#         "orientation": "PORTRAIT",
#         "automationName": "UiAutomator2",
#         "appWaitActivity": "com.wdiodemoapp.MainActivity",
#         "newCommandTimeout": 240
#     }
#     driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#     yield driver
# #     driver.quit()
