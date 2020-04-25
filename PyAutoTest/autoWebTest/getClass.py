'''
Created on Sep 29, 2019

@author: Sasa33k

'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Switcher(object):
    # Setup Get functions
    def Get(self, logger, browser, getParam = None, getMethod = None, winHandle = None):
        self.waitTimeout = 5
        self.browser = browser
        self.getMethod = getMethod
        self.getParam = getParam
        self.parent_handle = winHandle
        self.logger = logger
        logger.info("    ... Getting: " + str(getParam) + " " + str(getMethod))
        
        
        method=getattr(self, "By"+getMethod, lambda :'Invalid')
        self.new_handle = method;
        return method()
    
    
    def ByNewWin(self):    
        handles = self.browser.window_handles
        size = len(handles);
        for x in range(size):
            if handles[x] != self.parent_handle:
                self.logger.info("Switch to New Window...")
                self.logger.info(handles[x])
                self.browser.switch_to.window(handles[x])
                #print self.browser.title;
                #self.browser.close();
                return handles[x]
                break;
        return None
    
    def ByOriWin(self):
        self.logger.info("Switch to Original Window... ")
        self.logger.info(self.parent_handle)
        self.browser.switch_to.window(self.parent_handle)
        return None
    
    # Get By Actions
    def ById(self):
            element = WebDriverWait(self.browser, self.waitTimeout).until(
                EC.presence_of_element_located((By.ID, self.getParam))
            )
            return element
    
    def ByName(self):
            element = WebDriverWait(self.browser, self.waitTimeout).until(
                EC.presence_of_element_located((By.NAME, self.getParam))
            )
            return element
        
    
    def ByXpath(self):
            element = WebDriverWait(self.browser, self.waitTimeout).until(
                EC.presence_of_element_located((By.XPATH, self.getParam))
            )
            return element
        
    
    def ByLinkText(self):
            element = WebDriverWait(self.browser, self.waitTimeout).until(
                EC.presence_of_element_located((By.LINK_TEXT, self.getParam))
            )
            return element
        
    
    def ByPartialLinkText(self):
            element = WebDriverWait(self.browser, self.waitTimeout).until(
                EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, self.getParam))
            )
            return element
        
    def ByTagName(self):
            element = WebDriverWait(self.browser, self.waitTimeout).until(
                EC.presence_of_element_located((By.TAG_NAME, self.getParam))
            )
            return element
                
    def ByClassName(self):
            element = WebDriverWait(self.browser, self.waitTimeout).until(
                EC.presence_of_element_located((By.CLASS_NAME, self.getParam))
            )
            return element    
        
    def ByCssSelector(self):
            element = WebDriverWait(self.browser, self.waitTimeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.getParam))
            )
            return element

