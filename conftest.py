import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@pytest.fixture(scope='session')  # function or session
def driver():
    serv = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=serv)
    driver.maximize_window()
    yield driver
    driver.quit()
