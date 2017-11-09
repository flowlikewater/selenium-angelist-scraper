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

def scrapeKeyword(keyword_array):
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
    for i in range(len(keyword_array)):
        searchBox.send_keys(keyword_array[i])
        searchBox.send_keys(u'\ue007')
        print('text filled in searchbox')
        time.sleep((random.random() * 1))
    time.sleep(1+(random.random() * 2))
    
    # click on Joined button
    browser.find_element_by_xpath('//*[@id="root"]/div[4]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div[3]').click()
    print('joined button clicked')
    time.sleep(2+(random.random() * 2))

    # click on more button at bottom of page
    def clickTwentyTimes():
        # set range back to 20 when finished testing
        for _ in range(1):
            time.sleep((2+random.random() * 1))
            clickOnMore()
    def clickOnMore():
        browser.find_element_by_css_selector('div.more').click()
        print('more clicked')
    clickTwentyTimes()

    # identify rows to Scrape
    divs = browser.find_element_by_css_selector('div.results')
    rows = divs.find_elements_by_class_name("startup")
    print rows

    # print row name and href by row
    for row in rows:
        name = row.find_elements_by_class_name("startup-link")[1].get_attribute('innerHTML')
        href = row.find_elements_by_class_name("startup-link")[1].get_attribute('href')
        location = row.find_element_by_class_name("location").find_element_by_class_name("value")
        try:
            location_exists = location.find_element_by_tag_name("a").get_attribute('innerHTML')
            location = location_exists
        except: 
            location = 'n/a'
        print name 
        print href
        print location

keywords_to_scrape = [['AI'],['AI', 'Asia'],['AI', 'Japan']]

scrapeKeyword(keywords_to_scrape[0])

