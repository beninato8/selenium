from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
from bs4 import BeautifulSoup
import requests
from knightbooktext import htmldoc
import re

def printDetails(html):

    soup = BeautifulSoup(html, 'html.parser')
    parentString = ""
    parentType = ""
    parentName = ""
    c = []
    contactdict = {}
    address = ""
    advo = []
    for parent in soup.find_all('div', class_='remodal-wrapper remodal-is-opened'):
        for info in parent.find_all('div', class_='modal-student-info'):
            # print(info)
            for name in info.find_all('div', class_='name'):
                print('Name:', name.text)
            for grade in info.find_all('div', class_='grade'):
                print('Grade:', grade.text.split(' ')[0])
            for parents in info.find_all(class_='open-profile-details'):
            # for parents in info.find_all(class_=['open-profile-details', 'profile-details']):
                if 'advocacy' not in parents.parent.text.lower():
                    parentString = parents.parent.text.split('\n')[0]
                    parentName = parentString[:-6]
                    parentType = parentString[-6:]
                    print(parentType.title() + ": " + parentName)
                    # print('parents.parents', vars(parents.parent), 'end')
                    c = parents.parent.contents
                    c = c[c.index('\n')+1:-1]
                    matches = [x[1:-1] for x in re.findall(r'>[^<]+<', str(c[0]))][1:-1]
                    contactdict = {'email':[x for x in matches if re.match(r'.+@.+', x)], 
                                   'phone':[x for x in matches if re.match(r'.+-.+-.+|home|cell|work', x.lower())][::-1]}
                    print(contactdict)
                elif 'advocacy' in parents.parent.text.lower():
                    advo = [x[1:-1] for x in re.findall(r'>[^<]+<', str(parents.parent)) if x not in ('>\n<')]
                    print(advo[1] + ': ' + advo[2])
            for field in info.find_all('h4'):
                if 'address' in field.text.lower():
                    address = [x[1:-1] for x in re.findall(r'>[^<]+<', str(field.parent)) if x not in ('>\n<')]
                    print(address[0] + ': ' + ', '.join(address[1:]))
                if 'birthday' in field.text.lower():
                    print('Birthday:', field.parent.text[len('Birthday')+1:])
            for atag in info.find_all('a'):
                if '@menloschool.org' in atag.text:
                    print('Email: ', atag.text)

        print('*********************')

if True:
    d = 'x'
    if d == 'c':
        driver = '../chromedriver'
        browser = webdriver.Chrome(driver)
    else:
        driver = '../phantomjs'
        browser = webdriver.PhantomJS(driver)

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

    for currentID in idlist:
        curl = url+currentID
        # print(curl)
        browser.get(curl)
        browser.refresh()
        html = browser.page_source
        # print(html.encode('utf8'))
        print('UserID:', currentID)
        printDetails(html)

browser.quit()