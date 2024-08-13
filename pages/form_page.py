import os
from selenium.webdriver import Keys
from generator.generator import generated_person, generate_file
from locators.form_page_locators import FormPageLocators
from pages.base_page import BasePage


class FormPage(BasePage):
    locators= FormPageLocators()

    def fill_form_fields (self):
        person = next(generated_person())
        file_name, path = generate_file()
        self.element_is_visable(self.locators.FIRST_NAME).send_keys(person.firstname)
        self.element_is_visable(self.locators.LAST_NAME).send_keys(person.lastname)
        self.element_is_visable(self.locators.EMAIL).send_keys(person.email)
        self.element_is_visable(self.locators.GENDER).click()
        self.element_is_visable(self.locators.MOBILE).send_keys(person.mobile)
        self.element_is_visable(self.locators.SUBJECT).send_keys('Maths')
        self.element_is_visable(self.locators.SUBJECT).send_keys(Keys.RETURN)
        self.element_is_visable(self.locators.HOBBIES).click()
        self.element_is_present(self.locators.FILE_INPUT).send_keys(path)
        os.remove(path)
        self.element_is_visable(self.locators.CURRENT_ADDRESS).send_keys(person.current_address)
        self.element_is_visable(self.locators.SELECT_STATE).click()
        self.element_is_visable(self.locators.STATE_INPUT).send_keys(Keys.RETURN)
        self.element_is_visable(self.locators.SELECT_CITY).click()
        self.element_is_visable(self.locators.CITY_INPUT).send_keys(Keys.RETURN)
        self.element_is_visable(self.locators.SUBMIT).click()
        return person

    def form_result(self):
        result_list = self.elements_are_present(self.locators.RESULT_TABLE)
        data = []
        for item in result_list:
            self.go_to_element(item)
            data.append(item.text)
        return data












