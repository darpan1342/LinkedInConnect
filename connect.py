import time
import credentials
from selenium import webdriver

username = credentials.username()
passwd = credentials.passwd()
keywords = credentials.keywords()
browser = webdriver.Chrome(
    executable_path="C:\Program Files (x86)\Google\chrome\chromedriver.exe")

# loading linkedin sign in page
web_url = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
browser.get(web_url)

# passwd fill
input = browser.find_element_by_id('password')
input.send_keys(passwd)

# usernamefill
input = browser.find_element_by_id('username')
input.send_keys(username)

# signin
sign_in = browser.find_element_by_tag_name('Button')
sign_in.click()

# search_url
search_url = "https://www.linkedin.com/search/results/people/?facetNetwork=%5B\"S\"%2C\"O\"%5D&keywords="+keywords+"&origin=SWITCH_SEARCH_VERTICAL"
browser.get(search_url)

# full screen
browser.fullscreen_window()

exit
time.sleep(10)

# hiding msg window not needed for fullscreen
k = browser.find_element_by_class_name("msg-overlay-bubble-header__button")
k.click()

# fecthing buttons
it = browser.find_elements_by_tag_name("button")
j = 0
for i in it:
    if(i.text == "Connect"):
        j = j+1
        i.click()
        time.sleep(2)
        k = browser.find_element_by_class_name("ml1")
        k.click()

browser.close()
print(str(j)+" invites has been sent on your behalf.")
