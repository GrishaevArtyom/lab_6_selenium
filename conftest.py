import pytest
import os
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser():
    # Получаем путь от webdriver-manager
    driver_manager_path = ChromeDriverManager().install()

    # Если это папка (как в v3), ищем chromedriver внутри
    if os.path.isdir(driver_manager_path):
        candidate = Path(driver_manager_path) / "chromedriver"
        if candidate.exists():
            driver_path = str(candidate)
        else:
            raise RuntimeError(f"Could not find chromedriver in {driver_manager_path}")
    else:
        driver_path = driver_manager_path  # уже бинарник

    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")

    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def base_url():
    return "https://ya.ru"
