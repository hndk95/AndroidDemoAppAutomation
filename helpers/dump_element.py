from appium import webdriver
from appium.options.android import UiAutomator2Options
import time
from xml.etree import ElementTree

# Setup Appium
options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "RR8M40ZMHMD"
options.automation_name = "UiAutomator2"
options.app = "/Users/indrahandika/android-automation/app/Android-MyDemoAppRN.1.3.0.build-244.apk"
options.app_wait_activity = "*.*"
options.new_command_timeout = 300

driver = webdriver.Remote("http://0.0.0.0:4723", options=options)
time.sleep(5)

# Ambil page source
source = driver.page_source
root = ElementTree.fromstring(source)

# Simpan hasil ke file
output_lines = []

def walk(node, xpath=""):
    attrs = node.attrib
    clickable = attrs.get('clickable', 'false')
    current_xpath = f"{xpath}/{node.tag}[@resource-id='{attrs.get('resource-id', '')}']"

    line = f"{'🟢' if clickable == 'true' else '⚪'} Text: {attrs.get('text', '')}\n"
    line += f"🆔  Resource-ID: {attrs.get('resource-id', '')}\n"
    line += f"📍 XPath: {current_xpath}\n"
    line += "-" * 100
    output_lines.append(line)

    for child in node:
        walk(child, xpath + "/" + node.tag)

walk(root)

# Tulis ke file
with open("dump_elemen.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(output_lines))

print("📄 Elemen berhasil disimpan ke file dump_elemen.txt")

# Klik elemen dengan resource-id
def click_by_id(resource_id):
    try:
        el = driver.find_element("id", resource_id)
        el.click()
        print(f"✅ Klik elemen dengan ID: {resource_id}")
    except Exception as e:
        print(f"❌ Gagal klik elemen dengan ID {resource_id}: {e}")

# Klik elemen dengan XPath
def click_by_xpath(xpath):
    try:
        el = driver.find_element("xpath", xpath)
        el.click()
        print(f"✅ Klik elemen dengan XPath: {xpath}")
    except Exception as e:
        print(f"❌ Gagal klik elemen dengan XPath {xpath}: {e}")

# Klik elemen dengan Text
def click_by_text(text_value):
    try:
        xpath = f"//android.widget.TextView[@text='{text_value}']"
        el = driver.find_element("xpath", xpath)
        el.click()
        print(f"✅ Klik elemen dengan Text: {text_value}")
    except Exception as e:
        print(f"❌ Gagal klik elemen dengan Text '{text_value}': {e}")


# Contoh penggunaan (kamu bisa ganti sesuai elemen yang muncul di file)
# click_by_id("com.saucelabs.mydemoapp.rn:id/loginBtn")
# click_by_xpath("//android.widget.Button[@content-desc='Login']")

# Tutup driver
driver.quit()
