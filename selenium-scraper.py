# tutorial from http://thiagomarzagao.com/2013/11/12/webscraping-with-selenium-part-1/

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import random
import time 

path_to_log = '/Users/kevin/Documents/coding/Zeroth/Projects/Scrape/'
log_errors = open(path_to_log + 'log_errors.txt', mode = 'w')

path_to_chromedriver = '/Users/kevin/Documents/coding/Zeroth/Projects/Scrape/chromedriver' # change path as needed
browser = webdriver.Chrome(executable_path = path_to_chromedriver)

url = 'https://angel.co/companies'
browser.get(url)

# capture image only when javascript fully loads
WebDriverWait(browser, 120).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.more")))
print('more found')
time.sleep((random.random() * 2))

# fill in text in searchbox
# browser.find_element_by_css_selector('input.input.keyword-input').click()
browser.find_element_by_css_selector('div.search-box').click()
searchBox = browser.find_element_by_css_selector('input.input.keyword-input')
searchBox.clear()
searchBox.send_keys('AI')
searchBox.send_keys(u'\ue007')
print('text filled in searchbox')
time.sleep((random.random() * 2))

# click on Joined button
browser.find_element_by_xpath('//*[@id="root"]/div[4]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div[3]').click()
print('joined button clicked')
time.sleep((random.random() * 2))

# click on more button at bottom of page
browser.find_element_by_css_selector('div.more').click()
print('more clicked')

# browser.switch_to_frame('mainFrame')
# ensure selenium wauts fir a few seconds before it gives up finding elements
# method 1
    # browser.implicitly_wait(30)
# method 2
    # from selenium.webdriver.common.by import By
    # from selenium.webdriver.support.ui import WebDriverWait
    # import selenium.webdriver.support.expected_conditions as EC
    # from selenium.common.exceptions import TimeoutException
    # some_object = WebDriverWait(browser, 120).until(EC.element_to_be_located((By.CSS_SELECTOR, 'img[alt=\"Some Button\"]')))
    # try:
    #     some_object = WebDriverWait(browser, 120).until(EC.element_to_be_located((By.CSS_SELECTOR, 'img[alt=\"Some Button\"]')))
    #       or
    #     some_object = WebDriverWait(browser, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'img[alt=\"Some Button\"]')))
    #       or
    #     read all wait functions: http://selenium-python.readthedocs.io/waits.html
    # except TimeoutException:
    #     do something (retry, move on, exit, curse your internet provider, etc)
    #     log_errors.write('couldnt locate button XYZ when searching for "balloon"' + '\n')
# browser.find_element_by_id('terms')
# browser.find_element_by_id('terms').clear()
# browser.find_element_by_id('terms').send_keys('balloon')
# browser.find_element_by_xpath('//*[@id="srchButt"]').click()
# # browser.find_element_by_xpath('//*[@id="ddlDateOptions"]/option[contains(text(), "Today")]').click()
# # browser.find_element_by_xpath('//*[@id="OkButt"]').click()
# browser.switch_to_default_content()
# browser.switch_to_frame('mainFrame')
# browser.find_element_by_xpath('//*[@id="webId"]').clear()
# browser.find_element_by_xpath('//*[@id="webId"]').send_keys('kevkev')
# browser.quit()
