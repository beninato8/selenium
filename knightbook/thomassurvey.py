from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from bs4 import BeautifulSoup
import requests
from time import sleep

d = False
# d = True
if d:
    driver = '../phantomjs'
    browser = webdriver.PhantomJS(driver)
else:
    driver = '../chromedriver'
    browser = webdriver.Chrome(driver)

url = 'http://menloclarus.com/?id=' + "%07d" % (0000000)
start = 'http://menloclarus.com/?id='
# print(url)

# browser.get(url)
# browser.save_screenshot('img01.png')
# browser.find_element_by_xpath('//*[@id="submit"]').click()
# browser.save_screenshot('img02.png')

# if 'Invalid' in browser.page_source:
#     print('invalid')
# # exit()
# browser.quit()
valid = []
for i in range(0, 9999999):
    num = "%07d" % i
    browser.get(start + num)
    browser.set_window_size(1120, 550)
    browser.save_screenshot('img01.png')
    # browser.find_element_by_xpath('//*[@id="submit"]').click()
    element = WebDriverWait(browser, 1000).until(
            EC.presence_of_element_located((By.ID, "submit")))
    element.click()
    browser.save_screenshot('img02.png')
    # exit()
    sleep(1)
    if 'Invalid' not in browser.page_source:
        valid.append(num)
        print(num)
    if i % 10 == 0:
        print('**', num, '**')
    # exit()

