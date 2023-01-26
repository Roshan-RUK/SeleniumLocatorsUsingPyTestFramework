from selenium.webdriver.common.by import By

from pageObjects.CheckOutPage import CheckOutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkBox = (By.ID, "exampleCheck1")
    radioButton = (By.CSS_SELECTOR, "#inlineRadio1")
    selectDropDown = (By.ID, "exampleFormControlSelect1")
    submitButton = (By.XPATH, "//input[@type='submit']")
    successMessage = (By.CLASS_NAME, "alert-success")
    textBoxData = (By.XPATH, "(//input[@type='text'])[3]")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        check_out_page = CheckOutPage(self.driver)
        return check_out_page

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def clickCheckBox(self):
        return self.driver.find_element(*HomePage.checkBox)

    def selectRadioButton(self):
        return self.driver.find_element(*HomePage.radioButton)

    def selectAnDropDown(self):
        return self.driver.find_element(*HomePage.selectDropDown)

    def clickSubmit(self):
        return self.driver.find_element(*HomePage.submitButton)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage)

    def getTextBoxData(self):
        return self.driver.find_element(*HomePage.textBoxData)
