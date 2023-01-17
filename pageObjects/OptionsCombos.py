import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from testData.SeleniumPracticeData import SeleniumPracticeData


class OptionsCombos:
    def __init__(self, driver):
        self.driver = driver
    radioButton = (By.XPATH, "//input[@class='radioButton']")
    checkBox = (By.CSS_SELECTOR, "input[type='checkbox']")
    dynamicCombo = (By.XPATH, "//li[@class='ui-menu-item']/div")
    countryValue = (By.ID, "autocomplete")
    staticCombo = (By.XPATH, "//fieldset/select")

    def perform_optionsRadio(self, radioOption):
        radio_options = self.driver.find_elements(*OptionsCombos.radioButton)
        for each_option in radio_options:
            if each_option.get_attribute("value") == radioOption:
                each_option.click()

    def perform_optionsCheckBox(self, checkBox):
        checkbox_options = self.driver.find_elements(*OptionsCombos.checkBox)
        for each_checkBox in checkbox_options:
            if each_checkBox.get_attribute("value") == checkBox:
                each_checkBox.click()

    def perform_dynamicCombo(self, country):
        self.driver.find_element(*OptionsCombos.countryValue).send_keys(country)
        each_countrylist = self.driver.find_elements(*OptionsCombos.dynamicCombo)
        for each_country in each_countrylist:
            if each_country.text == country:
                each_country.click()

    def perform_staticCombo(self, staticOption):
        static_Dropdown = Select(self.driver.find_element(*OptionsCombos.staticCombo))
        static_Dropdown.select_by_visible_text(staticOption)





