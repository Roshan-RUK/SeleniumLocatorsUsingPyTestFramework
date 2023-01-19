from selenium.webdriver.common.by import By


class ActionsiFrames:
    def __init__(self,driver):
        self.driver = driver

    button = (By.ID, "mousehover")
    list = (By.CSS_SELECTOR, ".mouse-hover-content a:nth-child(1)")
    frameID = "courses-iframe"
    consult = (By.CSS_SELECTOR, "a[href*='consult']")

    def perform_moveButton(self):
        return self.driver.find_element(*ActionsiFrames.button)

    def perform_moveList(self):
        return self.driver.find_element(*ActionsiFrames.list)

    def perform_switchTOFrame(self):
        return self.driver.switch_to.frame(ActionsiFrames.frameID)

    def perform_selectConsult(self):
        return self.driver.find_element(*ActionsiFrames.consult)

