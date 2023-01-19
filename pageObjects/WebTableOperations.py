from selenium.webdriver.common.by import By

from pageObjects.ActioniFrames import ActionsiFrames


class WebTableOperations:
    def __init__(self, driver):
        self.driver = driver

    price = (By.XPATH, "//table[@class='table-display']/tbody/tr/td[3]")
    midScroll = "window.scrollBy(0,600);"
    topScroll = "document.querySelector('.tableFixHead').scrollTop=5000;"
    tableName = (By.CSS_SELECTOR, ".tableFixHead td:nth-child(1)")

    def perform_getAllPrices(self):
        return self.driver.find_elements(*WebTableOperations.price)

    def perform_windowScroll(self):
        return self.driver.execute_script(WebTableOperations.midScroll)

    def perform_InsideWindowScrollTop(self):
        return self.driver.execute_script(WebTableOperations.topScroll)

    def perform_getAllNames(self):
        self.driver.find_elements(*WebTableOperations.tableName)
        actionFrames_obj = ActionsiFrames(self.driver)
        return actionFrames_obj, self.driver.find_elements(*WebTableOperations.tableName)



