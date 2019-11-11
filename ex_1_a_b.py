from re import *
from selenium import webdriver
import time

def test_a(case_sens):
    url = 'https://markjs.io/configurator.html'

    re_str = 'lorem'
    form_context = '//*[@id="keyword"]'
    form_outcome = '/html/body/div[1]/main/div[1]/div[2]/div/div[2]'
    case_sens_chk = '//*[@id="form-keyword-caseSensitive"]'
    dia_chk = '//*[@id="form-keyword-diacritics"]'
    sbm_button = '/html/body/div[1]/main/div[1]/div[1]/div/div[2]/form[1]/button'

    driver = webdriver.Chrome()
    driver.get(url)

    driver.find_element_by_xpath(form_context).clear()
    driver.find_element_by_xpath(form_context).send_keys(re_str)

    is_checked = driver.find_element_by_xpath(case_sens_chk).is_selected()

    if is_checked and case_sens=='N':
        driver.find_element_by_xpath(case_sens_chk).click()
    if not is_checked and case_sens == 'Y':
        driver.find_element_by_xpath(case_sens_chk).click()

    if driver.find_element_by_xpath(dia_chk).is_selected():
        driver.find_element_by_xpath(dia_chk).click()

    driver.find_element_by_xpath(sbm_button).click()

    result_form = driver.find_element_by_xpath(form_outcome)
    tx_r = result_form.text

    if case_sens=='N':
        act_num = test_a_get_matches(tx_r)
        expected_number = 7
        assert act_num==expected_number

    if case_sens=='Y':
        act_num = test_b_get_matches(tx_r)
        expected_number = 1
        assert act_num == expected_number

    time.sleep(4)
    driver.quit()

def test_a_get_matches(result_string):

    iter = finditer('lorem', result_string, IGNORECASE)
    count=0
    for i in iter: count+=1
    print ("Your count is without case sensitivity is: ", count)
    return count

def test_b_get_matches(result_string):
    iter = finditer('lorem', result_string)
    count = 0
    for i in iter: count += 1
    print("Your count is with case sensitivity is: ", count)
    return count

# test_a('Y')

test_a("N")