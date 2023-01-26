
import time

import pytest
from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        home_Page = HomePage(self.driver)
        home_Page.getName().send_keys(getData["FirstName"])
        home_Page.getEmail().send_keys(getData["Email"])
        home_Page.getPassword().send_keys(getData["Password"])
        home_Page.clickCheckBox().click()
        home_Page.selectRadioButton().click()
        # Static dropdown
        self.selectOptionByText(home_Page.selectAnDropDown(), getData["Gender"])
        time.sleep(2)
        home_Page.clickSubmit().click()
        message = home_Page.getSuccessMessage().text
        print(message)
        assert "Success" in message
        home_Page.getTextBoxData().send_keys(getData["FirstName"])
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_Data)
    def getData(self, request):
        return request.param


