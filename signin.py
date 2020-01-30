from selenium import webdriver
import time
browser = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\chrome\chromedriver.exe")
web_url = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
browser.get(web_url)

#help(browser)
#sleep(5
browser.close()