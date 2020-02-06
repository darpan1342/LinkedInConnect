import time
from selenium import webdriver
import linkedin_bot

browser = linkedin_bot.setup()

search_url = "https://www.linkedin.com/mynetwork/invitation-manager/sent/"
browser.get(search_url)
time.sleep(2)

chec = browser.find_elements_by_class_name("ember-checkbox")
chec.pop(0)
withdraw = browser.find_elements_by_tag_name("time")
j = 0
time.sleep(1)

for i in withdraw:
    t = 0
    t_list = i.text
    t_list = t_list.split(" ")
    if t_list[1] == "hours":
        t = int(t_list[0])*0.1
    else:
        t = int(t_list[0]) 
    if t >= 5:
        action = webdriver.common.action_chains.ActionChains(browser)
        action.move_to_element_with_offset(chec[j],0,0)
        action.click()
        action.perform()
    j = j+1

try:
    n = browser.find_element_by_css_selector("button[data-control-name='withdraw_selected']")
    browser.execute_script("window.scrollTo(0,-document.body.scrollHeight)")

    n.click()
    time.sleep(2)

    n = browser.find_element_by_class_name("artdeco-modal__confirm-dialog-btn.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view")
    n.click()

except:
    print("No connection to withdraw.")

browser.close()