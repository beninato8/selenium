from selenium import webdriver
import re

phantomjs = '/Users/Nicholas/GitHub/beninato8-P1-PythonML/not classwork/phantomjs'
driver = webdriver.PhantomJS(phantomjs)

driver.set_window_size(1920,1080)

try:
    driver.get('https://google.com/search?q=what+is+my+ip')
    driver.find_element_by_xpath("//*[@type='submit']").click()
    content = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div[1]/w-answer/w-answer-desktop/div[1]').text
    print(content)
except:
    driver.save_screenshot('screenshot.png')
driver.quit()