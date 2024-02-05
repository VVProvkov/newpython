
import time
import sys

sys.path.append("../newpython")


from pages.base_page import BasePage
from conftest import driver

driver2 = driver

def test(driver):
    page = BasePage(driver2, 'https://www.google.com')
    page.open()
    time.sleep(3)