import pytest
import os
import datetime
import logging
import base64
from pytest_html import extras

from appium import webdriver
from appium.options.android import UiAutomator2Options

# ==== Logging Config ====
def setup_logger():
    logs_dir = os.path.join("reports", "logs")
    os.makedirs(logs_dir, exist_ok=True)
    log_file = os.path.join(logs_dir, "test_log.log")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

setup_logger()

# ==== Appium Driver Fixture ====
@pytest.fixture(scope="function")
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    # options.device_name = "RR8M40ZMHMD" 
    options.device_name = "emulator-5554" 
    options.automation_name = "UiAutomator2"
    options.app = os.path.abspath("app/Android-MyDemoAppRN.1.3.0.build-244.apk")
    options.app_wait_activity = "*.*"
    options.new_command_timeout = 300
    options.set_capability("uiautomator2ServerInstallTimeout", 60000)

    driver = webdriver.Remote("http://localhost:4723", options=options)
    logging.info("🔌 Appium driver started.")
    yield driver
    driver.quit()
    logging.info("❎ Appium driver quit.")

# ==== Screenshot on Fail + HTML Report Integration ====
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            test_name = item.name
            screenshot_dir = os.path.join("reports", "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, f"{test_name}_{timestamp}.png")
            driver.save_screenshot(screenshot_path)
            logging.error(f"📸 Screenshot captured: {screenshot_path}")

            # Embed screenshot into HTML report
            with open(screenshot_path, "rb") as image_file:
                encoded_img = base64.b64encode(image_file.read()).decode()
            html_extra = extras.html(
                f'<div><img src="data:image/png;base64,{encoded_img}" style="width:300px;" /></div>'
            )

            if not hasattr(rep, "extra") or not isinstance(rep.extra, list):
                rep.extra = []
            rep.extra.append(html_extra)

# ==== Create report folders if not exist ====
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    os.makedirs("reports/screenshots", exist_ok=True)
    os.makedirs("reports/logs", exist_ok=True)
