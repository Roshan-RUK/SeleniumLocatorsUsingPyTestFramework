from selenium.webdriver.common.by import By

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass

class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        self.driver.implicitly_wait(4)
        home_page = HomePage(self.driver)
        check_out_page = home_page.shopItems()
        log.info("Getting all the cart Titles")
        #check_out_page = CheckOutPage(self.driver)
        item_elements = check_out_page.getCardTitle()
        list_size = len(item_elements)
        for each_item in item_elements:
            #if each_item.find_element(check_out_page.productName).text == "Blackberry":
            if each_item.find_element(By.XPATH, "div/h4/a").text == "Blackberry":
                each_item.find_element(By.XPATH, "div/button").click()
        check_out_page.clickCheckOutbtn().click()
        confirm_page = check_out_page.clickCheckOutBtnFinal()
        #confirm_page = ConfirmPage(self.driver)
        confirm_page.enterCountryName().send_keys("ind")
        log.info("Entering country name")
        self.verifyLinkPresence("India")
        confirm_page.countryName().click()
        log.info("Selecting Country name from the list")
        confirm_page.checkBox().click()
        confirm_page.selectSubmit().click()
        log.info("Submitting the items from cart")
        success_text = confirm_page.confirmMessage().text
        assert "Success!" in success_text


