import time
import platform
from selenium import webdriver


def setup():

    pltfrm = platform.system()

    username = ""
    passwd = ""

    # windows
    if pltfrm == "Windows":
        browser = webdriver.Chrome(
            executable_path="C:\Program Files (x86)\Google\chrome\chromedriver.exe")
    else:
        # mac
        browser = webdriver.Chrome(
            executable_path="chrome_driver/chromedriver")

    # full screen
    browser.fullscreen_window()

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

    time.sleep(2)
    
    #get_url = browser.current_url()
    #if get_url != "https://www.linkedin.com/feed/":
    #    browser.close()

    return browser


if __name__ == "__main__":
    print("run connect.py or setup.py")
