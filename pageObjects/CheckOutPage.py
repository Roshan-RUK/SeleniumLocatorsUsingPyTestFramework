from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    productName = (By.XPATH, "div/h4/a")
    buttonCheckOut = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    buttonCheckOutFinal = (By.XPATH, "//button[@class='btn btn-success']")

    def __init__(self, driver):
        self.driver = driver

    def getCardTitle(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def clickCheckOutbtn(self):
        return self.driver.find_element(*CheckOutPage.buttonCheckOut)

    def clickCheckOutBtnFinal(self):
        self.driver.find_element(*CheckOutPage.buttonCheckOutFinal).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page
