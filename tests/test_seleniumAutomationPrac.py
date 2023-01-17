import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.OptionsCombos import OptionsCombos
from testData.SeleniumPracticeData import SeleniumPracticeData
from utilities.BaseClass import BaseClass


class TestSeleniumAutoPrac(BaseClass):
    def test_seleniumAutomationPractice(self, getData):
        log = self.getLogger()
        self.driver.implicitly_wait(4)
        optionCombos_obj = OptionsCombos(self.driver)
        optionCombos_obj.perform_optionsRadio(getData["radio"])
        log.info("After Radio Option")
        optionCombos_obj.perform_optionsCheckBox(getData["checkBox"])
        log.info("After CheckBox Option")
        optionCombos_obj.perform_dynamicCombo(getData["country"])
        log.info("After Dynamic Combo box")
        optionCombos_obj.perform_staticCombo(getData["selectCombo"])
        log.info("After Select combo box")
        time.sleep(2)

    @pytest.fixture(params=SeleniumPracticeData.selenium_practice_data)
    def getData(self, request):
        return request.param

