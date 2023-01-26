from selenium.webdriver.common.by import By


class ConfirmPage:
    country = (By.ID, "country")
    selectCountryName = (By.LINK_TEXT, "India")
    selectCheckBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submit = (By.CSS_SELECTOR, "[type='submit']")
    successMessage =(By.CLASS_NAME, "alert-success")

    def __init__(self, driver):
        self.driver = driver

    def enterCountryName(self):
        return self.driver.find_element(*ConfirmPage.country)

    def countryName(self):
        return self.driver.find_element(*ConfirmPage.selectCountryName)

    def checkBox(self):
        return self.driver.find_element(*ConfirmPage.selectCheckBox)

    def selectSubmit(self):
        return self.driver.find_element(*ConfirmPage.submit)

    def confirmMessage(self):
        return self.driver.find_element(*ConfirmPage.successMessage)
