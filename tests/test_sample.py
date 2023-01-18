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
    driver.maximize_window()
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
    driver.find_element(By.ID, "openwindow").click()
    windows_opened = driver.window_handles
    driver.switch_to.window(windows_opened[1])
    title = driver.title
    assert "QA Click" in title
    driver.close()
    driver.switch_to.window(windows_opened[0])
    print(driver.title+"\nInside Parent Window")
    driver.find_element(By.ID, "opentab").click()
    Tab_open = driver.window_handles
    driver.switch_to.window(Tab_open[1])
    tab_title= driver.title
    assert "Rahul" in tab_title
    driver.close()
    driver.switch_to.window(Tab_open[0])
    print(driver.title + "\nInside Parent Tab")
    driver.find_element(By.NAME, "enter-name").send_keys("Roshan")
    driver.find_element(By.ID, "alertbtn").click()
    alert_data = driver.switch_to.alert
    alert_text = alert_data.text
    assert "Roshan" in alert_text
    alert_data.accept()
    price_elements = driver.find_elements(By.XPATH, "//table[@class='table-display']/tbody/tr/td[3]")
    sum = 0
    for each_price in price_elements:
        sum = sum + int(each_price.text)
    print(sum)
    driver.execute_script("window.scrollBy(0,600);")
    driver.execute_script("document.querySelector('.tableFixHead').scrollTop=5000;")
    table_names = driver.find_elements(By.CSS_SELECTOR, ".tableFixHead td:nth-child(1)")
    for each_name in table_names:
        if each_name.text == "Smith":
            print("Smith name found")


    time.sleep(2)



