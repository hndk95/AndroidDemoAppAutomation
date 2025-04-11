import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture(scope="function")
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "RR8M40ZMHMD"
    options.automation_name = "UiAutomator2"
    options.app = "./app/Android-MyDemoAppRN.1.3.0.build-244.apk"
    options.app_wait_activity = "*.*"
    options.new_command_timeout = 300
    options.set_capability("uiautomator2ServerInstallTimeout", 60000)

    driver = webdriver.Remote("http://0.0.0.0:4723", options=options)
    # driver = webdriver.Remote("http://localhost:4723", options=options)
    yield driver
    driver.quit()
