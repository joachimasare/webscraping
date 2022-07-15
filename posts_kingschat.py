from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

browser = webdriver.Chrome() #launchs browser

input("Please log in and press <Enter> to continue") #login page pops up, after log in, press 'Enter' key to proceed

browser.get("https://web.kingsch.at/communities/153/posts") #browser redirects to load page (posts page with post text area)

##text = driver.find_elements_by_xpath("//input[@name='lang' and @value='Python']")
text = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "textarea"))) #wait until text area is located 
photo_upload = browser.find_elements_by_class_name("CommunityNewPost__attachment") #locate image text arear


for i in range(10000): #iterate 10000 times
    try:
        sleep(2)
        text.send_keys("We have done it before and we did it again.\n ROR COMMEMORATIVE Edition \n #CeAccraGhanaZone #WeDIDitAgain #CeMadinaTeens") #enters text in quotes
        #submit = browser.find_elements_by_class_name("CommunityNewPost__new-post-submit-btn ripple")
        text = browser.find_element_by_name("new_post")
        submit = browser.find_element_by_class_name("CommunityNewPost__new-post-submit-btn")
        sleep(5)
        submit.click()
    except:
        print("Unexpected Failure")

    
