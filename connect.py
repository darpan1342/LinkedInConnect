import time
from selenium import webdriver
import linkedin_bot

browser = linkedin_bot.setup()

j = 0  # count for number invites sent
keywords = ["Python", "Data Analyst", "Machine Learning"]

for keyword in keywords:
    # search_url
    search_url = "https://www.linkedin.com/search/results/people/?facetNetwork=%5B\"S\"%2C\"O\"%5D&keywords=" + \
        keyword+"&origin=SWITCH_SEARCH_VERTICAL"
    browser.get(search_url)

    time.sleep(2)

    # hiding msg window not needed for fullscreen
    #k = browser.find_element_by_class_name("msg-overlay-bubble-header__button")
    # k.click()

    # fecthing buttons
    it = browser.find_elements_by_tag_name("button")

    for i in it:
        if(i.text == "Connect"):
            j = j+1
            i.click()
            time.sleep(2)
            k = browser.find_element_by_class_name("ml1")
            k.click()

browser.close()
print(str(j)+" invites has been sent on your behalf.")
