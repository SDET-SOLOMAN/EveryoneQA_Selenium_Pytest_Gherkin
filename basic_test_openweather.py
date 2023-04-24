from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


driver_path = ChromeDriverManager().install()
serv = Service(driver_path)
driver = webdriver.Chrome(service=serv)

driver.get("https://openweathermap.org/")

# find serach bar
search = driver.find_element(By.CSS_SELECTOR, "div.search-container input")
search.clear()
search.send_keys("New York", Keys.RETURN)

city_visible = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.search-container "
                                                                                                "li:nth-child("
                                                                                                "1)"))).click()

new_page = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.current-container"
                                                                                              ".mobile"
                                                                                   "-padding h2"), "New York City, US"))

expected = "New York"
actual = driver.find_element(By.CSS_SELECTOR, "div.current-container.mobile-padding h2").text
print(expected, actual)
assert expected in actual
