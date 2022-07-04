from selenium import webdriver
from selenium.webdriver.common.by import By
import time

if __name__ == '__main__':
    # website credentials
    username = "*****"
    password = "*****"

    # initialize the Chrome driver
    driver = webdriver.Chrome("chromedriver")

    # request library login page
    driver.get('https://schedule.tau.ac.il/scilib/Web/index.php')

    # find username field and send the username itself to the input field
    driver.find_element(By.ID, "email").send_keys(username)

    # find password input field and insert password as well
    driver.find_element(By.ID, "password").send_keys(password)

    # time.sleep(3)

    # click login button
    driver.find_element(By.XPATH, '//button[@name=\'login\']').click()

    # time.sleep(3)

    # request the page of the following week
    year = driver.find_element(By.XPATH, "//div[@class=\'schedule-dates col-sm-3 col-xs-12\']/a[3]").get_attribute('data-year')
    month = driver.find_element(By.XPATH, "//div[@class=\'schedule-dates col-sm-3 col-xs-12\']/a[3]").get_attribute('data-month')
    day = driver.find_element(By.XPATH, "//div[@class=\'schedule-dates col-sm-3 col-xs-12\']/a[3]").get_attribute('data-day')

    new_link = 'https://schedule.tau.ac.il/scilib/Web/schedule.php?sd=' + year + "-" + month + "-" + day
    driver.get(new_link)

    # time.sleep(3)

    # choose the desired room slot  ### CHANGEABLE - td red number in line 42 ###
    ref = year + month + day + "10000026"
    driver.find_element(By.XPATH, ("//td[@ref='" + ref + "']")).click()

    # time.sleep(3)

    # choose the desired period of time in the room ### CHANGEABLE - hour in line 50 ###
    element_selection = driver.find_element(By.ID, 'EndPeriod')
    for option in element_selection.find_elements(By.TAG_NAME, "option"):
        if option.get_attribute('value') == "13:00:00":
            option.click()
            break

    # time.sleep(3)

    # submit reservation
    driver.find_element(By.XPATH, '//button[@class=\'btn btn-success save create btnCreate\']').click()

    # time.sleep(10)
