'''
Created on Sep 28, 2019

@author: Sasa33k

'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("D:\drivers\chromedriver.exe")

browser.get('http://www.yahoo.com')
assert 'Yahoo' in browser.title

elem = browser.find_element_by_name('p')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)


browser.quit()

""""
class SeleniumBaseClass(object):
    def __init__(self,driver):
        self.driver = driver
    def open(self,URL):
        self.driver.get(URL)
    def driverURLChange(self,URL):  
        print("change URL" + URL)
        self.driver.get(URL)
    def currentUrl(self):
        print("URL   " +  self.driver.current_url)
        return self.driver.current_url
    def switchNewWindow(self):
        self.driver.switch_to_window(self.driver.window_handles[1])
        return self.driver.title
    def locateElement(self, loc):
        try:
            print(loc)
            element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return element
        except:
            print ("cannot find {0} element".format(loc))
        return None
and you could

password_loc =(By.NAME,'password')
webdriver = SeleniumBaseClass(driver)
webdriver.locateElement(password_loc )
"""