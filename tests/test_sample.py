import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#The file to write sample testing code

def test_sample():
    service_obj = Service("C:\ChromeDPython\chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.implicitly_wait(4)
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    radio_options = driver.find_elements(By.XPATH, "//input[@class='radioButton']")
    for each_option in radio_options:
        if each_option.get_attribute("value") == "radio2":
            each_option.click()
    checkbox_options = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
    for each_checkBox in checkbox_options:
        if each_checkBox.get_attribute("value") == "option3":
            each_checkBox.click()

    driver.find_element(By.ID, "autocomplete").send_keys("Ind")
    each_countrylist = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']/div")
    for each_country in each_countrylist:
        if each_country.text == "India":
            each_country.click()
    static_Dropdown = Select(driver.find_element(By.XPATH, "//fieldset/select"))
    static_Dropdown.select_by_visible_text("Option1")
    time.sleep(5)

