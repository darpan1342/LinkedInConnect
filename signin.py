from selenium import webdriver
import time

browser = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\chrome\chromedriver.exe")

#loading linkedin sign in page 
web_url = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
browser.get(web_url)

#passwd fill
input = browser.find_element_by_id('password')
input.send_keys('darpan123@sharma')

#usernamefill
input = browser.find_element_by_id('username')
input.send_keys('asharma6890@gmail.com')

#signin
sign_in = browser.find_element_by_tag_name('Button')
sign_in.click()

web_url = "https://www.linkedin.com/search/results/people/?keywords=python&origin=SWITCH_SEARCH_VERTICAL"
browser.get(web_url)

it = browser.find_elements_by_tag_name('code')
j=0
for i in it:
    j = j+1
print(j) 
#sleep(5)
#help(browser)

#browser.close()