from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
from bs4 import BeautifulSoup
import requests

chromedriver = './chromedriver'
browser = webdriver.Chrome(chromedriver)
browser.get('https://login.menloschool.org:8443/cas/login?service=https%3A%2F%2Fknightbook.menloschool.org%2F')

username = browser.find_element_by_id("username")
password = browser.find_element_by_id("password")

with open("/Users/Nicholas/GitHub/login.json", "r") as file:
  login = json.load(file)
username.send_keys(login['username'])
password.send_keys(login['password'])

login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
login_attempt.submit()

html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')

print(soup.prettify().encode('utf-8'))
#for tag in soup("div  "):
    #print(tag.encode('utf-8'))
for tag in soup.find_all('a'):
  print(tag)


