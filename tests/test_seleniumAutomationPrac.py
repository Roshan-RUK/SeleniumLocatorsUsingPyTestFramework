import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.OptionsCombos import OptionsCombos
from pageObjects.WindowsTabsAlerts import WindowTabAlert
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
        windowTabAlert_obj = optionCombos_obj.perform_staticCombo(getData["selectCombo"])
        log.info("After Select combo box")
        #Windows Tabs and Alerts
        windowTabAlert_obj.perform_WindowsOperation().click()
        windows_opened = self.driver.window_handles
        self.driver.switch_to.window(windows_opened[1])
        title = self.driver.title
        assert "QA Click" in title
        self.driver.close()
        self.driver.switch_to.window(windows_opened[0])
        print(self.driver.title + "\nInside Parent Window")
        log.info("After Windows Operation")
        windowTabAlert_obj.perform_TabsOperation().click()
        tab_open = self.driver.window_handles
        self.driver.switch_to.window(tab_open[1])
        tab_title = self.driver.title
        assert getData["pageTitle"] in tab_title
        self.driver.close()
        self.driver.switch_to.window(tab_open[0])
        print(self.driver.title + "\nInside Parent Tab")
        log.info("After Tabs Operation")
        windowTabAlert_obj.perform_AlertEnterOperation().send_keys(getData["alertValue"])
        windowTabAlert_obj.perform_AlertClickOperation().click()
        alert_data = self.driver.switch_to.alert
        alert_text = alert_data.text
        assert getData["alertValue"] in alert_text
        alert_data.accept()
        log.info("After Tabs Operation")
        time.sleep(2)

    @pytest.fixture(params=SeleniumPracticeData.selenium_practice_data)
    def getData(self, request):
        return request.param

