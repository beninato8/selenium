from selenium import webdriver
from time import sleep
import os
import random

os.system("python3 /Users/Nicholas/GitHub/beninato8-P1-PythonML/not\ classwork/proxy_req.py")
try:
    f = open('/Users/Nicholas/GitHub/beninato8-P1-PythonML/not classwork/proxy_file.txt')
    proxy_ip = f.read()
    f.close()
    if len(proxy_ip) <= 1:
        os.system("python3 /Users/Nicholas/GitHub/beninato8-P1-PythonML/not\ classwork/proxy_req.py")
    else: # Valid proxy
        print('Using proxy: ' + proxy_ip)
        PROXY = proxy_ip 
        service_args = [ 
            '--proxy=' + proxy_ip,
            '--proxy-type=socks5'
        ]
        print(service_args)
        driver = webdriver.PhantomJS(executable_path='/Users/Nicholas/GitHub/beninato8-P1-PythonML/not classwork/phantomjs', service_args=service_args) 
except: 
    os.system("python3 /Users/Nicholas/GitHub/beninato8-P1-PythonML/not\ classwork/proxy_req.py")
    print("REQUEST ERROR...No Proxy will be used...")
    driver = webdriver.PhantomJS('/Users/Nicholas/GitHub/beninato8-P1-PythonML/not classwork/phantomjs')
#driver.get("https://ipinfo.io/")
#driver.save_screenshot('ipinfo.png')

#driver.get('https://google.com/search?q=what+is+my+ip')
#driver.save_screenshot('google.png')
print('test')
driver.get('http://www.10best.com/awards/travel/makers-in-the-usa-best-food-drink-2017/charles-chocolates-chocolates/')

driver.save_screenshot('chocolate.png')
driver.find_element_by_id('awardVoteButton').click()
driver.save_screenshot('chocolate.png')
wait = random.randint(0,60)
print("Waiting " + str(wait) + " seconds")
#sleep(wait)
driver.quit()