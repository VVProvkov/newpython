import pytest
import time
from selenium import webdriver



#@pytest.fixture(scope='function')

def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    #yield driver
    #url="https://metanit.com/"
    driver.get(url)
    #time.sleep(3)
    driver.quit()

driver()