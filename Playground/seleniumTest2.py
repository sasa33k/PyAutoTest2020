'''
Created on Sep 28, 2019

@author: Sasa33k

'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

browser = webdriver.Chrome("D:\drivers\chromedriver.exe")

browser.get('https://imggmi.com/')
browser.find_element_by_id("file").send_keys('C:\\Users\\n0321235\\Downloads\\downloads.png')


#browser.file_detector("<>")
upload=browser.find_element_by_xpath('//*[@id="home"]/div[2]/div/div/div/div/button').click()

browser.find_element_by_id('fileUpload_newFileUpload_inputfileUpload').send_keys("download.png")
upload.send_keys("download.png")



keys=upload.send_keys("abc.png")
    
""" 
browser.find_element_by_xpath('//*[@id="home"]/div[2]/div/div/div/div/button').send_keys("download.png")
elem = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="home"]/div[2]/div/div/div/div/button'))
            )
print(elem)


parent_handle = browser.current_window_handle;

handles = browser.window_handles;
size = len(handles);

elem.click()
elem.send_keys('seleniumhq' + Keys.RETURN)

for x in range(size):
    if handles[x] != parent_handle:
        a = browser.switch_to.window(handles[x])
        #print browser.file_detector;
        browser.file_detector.send_keys('seleniumhq' + Keys.RETURN)
        browser.file
        #browser.close();
        break;

browser.switch_to.window(parent_handle);
"""
sleep(10)
browser.quit()