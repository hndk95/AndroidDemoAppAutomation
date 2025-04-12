# 📱 Demo App Android Automation

Automated mobile testing framework using **Python**, **Appium**, and **Pytest** with support for:

- 📦 Page Object Model (POM)
- 🧪 Screenshot on failure
- 📊 HTML & JSON test reports
- 📈 Visual test summary dashboard via Jupyter

## 📁 Project Structure

- `tests/` → test cases
- `pages/` → reusable page objects
- `locators/` → object repository
- `reports/` → auto-generated reports and screenshots
- `dashboard_test_report.ipynb` → test summary dashboard

## ▶️ How to Run

```bash
pip install -r requirements.txt
pytest --html=reports/report.html --self-contained-html --json-report --json-report-file=reports/result.json -s
