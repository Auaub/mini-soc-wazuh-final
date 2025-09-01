import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--ignore-certificate-errors")       # <--- Add this
    options.add_argument("--allow-insecure-localhost")        # <--- Add this
    service = Service("/usr/bin/chromedriver")  # adjust path if needed
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_dashboard_https(driver):
    driver.get("https://soc.local")
    assert "Wazuh" in driver.title or "Whoami" in driver.page_source
    assert driver.find_element(By.TAG_NAME, "form")  # login form exists

