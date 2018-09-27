from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
from bs4 import BeautifulSoup
import requests
from knightbooktext import htmldoc
import re
import sys
import numpy as np

d = False
d = True
if d:
    driver = '../phantomjs'
    browser = webdriver.PhantomJS(driver)
else:
    driver = '../chromedriver'
    browser = webdriver.Chrome(driver)

idlist = []
login = 'https://login.menloschool.org:8443/cas/login?service=https://knightbook.menloschool.org/'
url = 'https://knightbook.menloschool.org#'
with open('ids.txt', 'r', encoding='utf8') as ids:
    for line in ids:
        idlist.append(line.split(' ')[0])

browser.get(login)
username = browser.find_element_by_id("username")
password = browser.find_element_by_id("password")

with open("../../login.json", "r") as file:
    login = json.load(file)
username.send_keys(login['username'])
password.send_keys(login['password'])

login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
login_attempt.submit()

browser.get(url)
img1 = 'https://knightbook.menloschool.org/get_photo.php?rid='
img2 = '&ay=1718&s=l'

currentID = data[name]
curl = url+currentID
# print(curl)
browser.get(curl)
browser.refresh()
html = browser.page_source
# print(html.encode('utf8'))
print('UserID:', currentID)
printDetails(html)
# browser.get(img1+currentID+img2)
# browser.save_screenshot('./photos/' + name + '.png')

url = 'http://example.com/userinfo.php'
values = {'username': login['username'],
          'password': login['password']+'\n'}

headers = {
"User-Agent":
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
}
s = requests.session()
s.headers.update(headers)

for cookie in browser.get_cookies():
    c = {cookie['name']: cookie['value']}
    s.cookies.update(c)

r = s.get(img1+currentID+img2, allow_redirects=True)
open('./photos/' + name + '.jpeg', 'wb').write(r.content)
browser.quit()