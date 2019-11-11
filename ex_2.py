from re import *
from selenium import webdriver
import time
import json
from lxml import html
import requests

url = 'http://teroauralinna.github.io/vue-demo-form/'

message_1003 = 'Lorem ipsum dolor sit āmet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore ' \
            'et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. ' \
            'Stet clita kasd gubergren, one, nò sea takimata 1 sanctus est Lorem ipsum dolor sit amet. Lörem ipsum dolor ' \
            'sit amet, consetetur sadipscing elitr, sed diam lor­em ipsum nonumy eirmod tempor invidunt ut labore et ' \
            'dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. ' \
            'Stet clita kasd gubergren, no sea takimata sanctus est lorem ipsum dolor sit amet. Lorem ipsum dolor sit ' \
            'amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna ' \
            'aliquyam erat. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor ' \
            'invidunt ut labore et dolore magna aliquyam erat. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, ' \
            'sed diam nonumy. Lore"m ipsu%m dolor sit amet. Lo!rem ipsum.'
message_1000 = message_1003[:1000]
message_reg = message_1003[:500]
message_min = "a"

first_name ='//*[@id="firstName"]'
last_name ='//*[@id="lastName"]'
email_addr ='//*[@id="email"]'
additional ='//*[@id="additionalInfo"]'
concent_chk ='//*[@id="terms"]'
plan_choice ='//*[@id="type"]' #dropdown //*[@id="type"]/option[1]
sbm_button = '//*[@id="app"]/div/div/div/form/div[7]/button'
res_form = '//*[@id="app"]/div/div/div/div/div[2]/pre'
message_alert = '//*[@id="app"]/div/div/div/form/div[5]/small'
email_alert = '//*[@id="app"]/div/div/div/form/div[3]/div'
first_name_alert = '//*[@id="app"]/div/div/div/form/div[1]/div'
last_name_alert = '//*[@id="app"]/div/div/div/form/div[2]/div'
plan_choice_alert = '//*[@id="app"]/div/div/div/form/div[4]/div'
message_alert_length = "Message ois too long"
email_alert_text = "Email is invalid or missing."
plan_choice_alert_text = "Select subscription type"
first_name_alert_text = "First name is required"
last_name_alert_text = "Last name is required"


# Assumption 1: The name fields should have a defined length
# Assumption 2: Email should have a '@' and domain name (@something.ext)
# Assumption 3: Additional info should not go over 1000 chars (incl spaces).

# Positive scennario: Run end to end with permitted entries and submit, data on the submitted form equals entered data.

def test_pos_1():
    driver = webdriver.Chrome()
    driver.get(url)
    print (driver.title)
    enter_data(driver.find_element_by_xpath(first_name), 'Test')
    enter_data(driver.find_element_by_xpath(last_name), 'Monster')
    enter_data(driver.find_element_by_xpath(email_addr), 'test.monster@at.at')
    enter_data(driver.find_element_by_xpath(additional), message_1003)
    if driver.find_element_by_xpath(concent_chk).is_selected():
        pass
    else: driver.find_element_by_xpath(concent_chk).click()
    driver.find_element_by_xpath(plan_choice).click()
    driver.find_element_by_xpath(plan_choice+'/option[1]').click()

    driver.find_element_by_xpath(sbm_button).click()
    time.sleep(5)
    #print (driver.title)

    page = requests.get(url)
    #print (page)
    res_text = driver.find_element_by_xpath('//*[@id="app"]')
    #print ((res_text.text))

    dr1 = driver.find_elements_by_xpath('//*[@class="col-xs-12 col-sm-10 col-md-6"]')
    res_text = dr1# driver.find_element_by_xpath('//*[@class = "alert alert-info"]/div')
    a = (res_text[0].text).split('\n')


    assert a[0]==driver.title
    assert a[1]=='The form is submitted!'

    answ_dict = json.loads(''.join(a[3:11]))

    print (len(answ_dict['additionalInfo']))
    assert len(answ_dict['additionalInfo']) <= 1000
    assert answ_dict['firstName'] == 'Test'
    assert answ_dict['lastName'] == 'Monster'
    assert answ_dict['email'] == 'test.monster@at.at'


    driver.find_elements_by_xpath('//*[@href="#"]')[0].click()
    time.sleep(5)

    driver.quit()

def test_neg_1_message_length():
    driver = webdriver.Chrome()
    driver.get(url)
    print(driver.title)

    enter_data(driver.find_element_by_xpath(additional), message_1003)


    driver.find_element_by_xpath(sbm_button).click()

    assert driver.find_element_by_xpath(message_alert).text == message_alert_length
    assert driver.find_element_by_xpath(email_alert).text == email_alert_text
    assert driver.find_element_by_xpath(first_name_alert).text == first_name_alert_text
    assert driver.find_element_by_xpath(last_name_alert).text == last_name_alert_text
    assert driver.find_element_by_xpath(plan_choice_alert).text == plan_choice_alert_text
    #assert driver.find_element_by_xpath()
    print(driver.title)

    page = requests.get(url)
    print(page)
    res_text = driver.find_element_by_xpath('//*[@id="app"]')  # //*[@class = "alert alert-info"]/div')
    print(res_text)

def enter_data(elem, data):
    elem.clear()
    elem.send_keys(data)
    return

test_pos_1()

# test_neg_1_message_length()