from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "RR8M40ZMHMD"  # atau nama real device kamu
options.automation_name = "UiAutomator2"
options.app = "/Users/indrahandika/android-automation/app/Android-MyDemoAppRN.1.3.0.build-244.apk"
options.app_wait_activity = "*.*"
options.new_command_timeout = 300

# Tambahan timeout supaya Appium tidak error saat install UIAutomator2 server
options.set_capability("uiautomator2ServerInstallTimeout", 60000)

driver = webdriver.Remote("http://0.0.0.0:4723", options=options)

time.sleep(5)

print("✅ Aplikasi berhasil dibuka!")

driver.quit()
