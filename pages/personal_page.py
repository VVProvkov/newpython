from base.base_page import BasePage
import allure
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class PersonalPage(BasePage):

    PAGE_URL = Links.PERSONAL_PAGE
    FIRST_NAME_FIELD = ("xpath", "//input[@name='firstName']")
    SAVE_BUTTON = ("xpath", "(//button[@type='submit'])[1]")

    @allure.step("Enter login")
    def change_name(self, new_name):
        with allure.step("Change name on '{new_name}'"):
            first_name_field = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_FIELD)) # noqa
            first_name_field.clear()
            first_name_field.send_keys(new_name)
            self.name = new_name
    @allure.step("Save changes")
    def save_changes(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()


    @allure.step("Changes has been saved successfuly")
    def is_changes_saved(self):
        self.wait.until(EC.text_to_be_present_in_element_value(self.FIRST_NAME_FIELD, self.name)) # noqa
