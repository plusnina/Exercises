from selenium import webdriver
import time

def ex_3():
    driver = webdriver.Chrome()
    driver.get('https://giphy.com')

    dr = driver.find_elements_by_xpath('//*[@id="searchbar"]/div/div/form/input')
    enter_data(dr[0], 'fintech')
    subm = driver.find_elements_by_xpath('//*[@id="searchbar"]/div/a/div/div[2]')
    subm[0].click()
    time.sleep(5)
    driver.implicitly_wait()
    assert (driver.find_elements_by_xpath('//*[contains(text(), "cute")]'))
    driver.quit()

def enter_data(elem, data):
    elem.send_keys(data)
    return

ex_3()