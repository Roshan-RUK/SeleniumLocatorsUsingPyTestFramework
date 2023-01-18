from selenium.webdriver.common.by import By

from pageObjects.WebTableOperations import WebTableOperations


class WindowTabAlert:
    def __init__(self, driver):
        self.driver = driver

    window = (By.ID, "openwindow")
    tabs = (By.ID, "opentab")
    alertName = (By.NAME, "enter-name")
    alertCLick = (By.ID, "alertbtn")

    def perform_WindowsOperation(self):
        return self.driver.find_element(*WindowTabAlert.window)

    def perform_TabsOperation(self):
        return self.driver.find_element(*WindowTabAlert.tabs)

    def perform_AlertEnterOperation(self):
        return self.driver.find_element(*WindowTabAlert.alertName)

    def perform_AlertClickOperation(self):
        self.driver.find_element(*WindowTabAlert.alertCLick).click()
        webTableOps_Obj = WebTableOperations(self.driver)
        return webTableOps_Obj


