'''
Created on Sep 29, 2019

@author: Sasa33k

'''
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from PyAutoTest.common import commonUtil as util
from time import sleep
import PyAutoTest.common.GlobalParam as gp

class Switcher(object):
    # Setup Do functions
    def Do(self, logger, browser, element, DoAction, DoParamX, DoParamY):
        self.browser = browser
        self.element = element
        self.DoAction = DoAction
        self.DoParamX = DoParamX
        self.DoParamY = DoParamY
        self.logger = logger
        logger.info("    ... Doing: " + self.DoAction)
        method=getattr(self, DoAction, lambda :'Invalid')
        return method()


    # Do Actions
    def FetchPage(self):
        self.browser.get(self.DoParamX)
        return [True,""]
    
    def Wait(self):
        sleep(int(self.DoParamX))
        return [True,""]



    def SendKeys(self):
        self.element.send_keys(self.DoParamX)
        return [True,""]
    
    def ClearSendKeys(self):
        self.element.clear()
        self.element.send_keys(self.DoParamX)
        return [True,""]

    def SelectByText(self):
        Select(self.element).select_by_visible_text(self.DoParamX)
        return [True,""]

    def Click(self):
        self.element.click()
        return [True,""]
    
    def DoubleClick(self):
        self.element.doubleClick()
        return [True,""]
    
    def GetText(self):
        sleep(1)
        text = self.element.get_attribute("text")
        if(text == self.DoParamX or text == self.DoParamY):
            return [True, util.xstr(text)]
        else:
            return [False, "Actual Text found: " + util.xstr(text)]
        
    def GetAttribute(self):
        text = self.element.get_attribute(self.DoParamX)
        if(text == self.DoParamY):
            return [True, ""]
        else:
            return [False, "Actual Text found: " + util.xstr(text)]
    
    def Enter(self):
        self.element.send_keys(Keys.RETURN)
        return [True,""]

    def SaveParam(self):
        sleep(1)
        text = self.element.get_attribute(self.DoParamX)
        util.AddOrReplace(gp.savedParam, self.DoParamY, util.xstr(text))
        return [True, util.xstr(text)]
