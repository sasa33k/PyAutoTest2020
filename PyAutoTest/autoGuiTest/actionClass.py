'''
Created on Sep 29, 2019

@author: Sasa33k



'''
import pyautogui
from time import sleep
from PyAutoTest.common import commonUtil as util

def convertKey(txtKey):
    keySplit = txtKey.split(',')
    return keySplit
    
class Switcher(object):
    # Setup Do functions
    def Do(self, logger, element, DoAction, DoParamX, DoParamY):
        self.element = element
        self.DoAction = DoAction
        self.DoParamX = DoParamX
        self.DoParamY = DoParamY
        self.logger = logger
        logger.info("    ... Doing: " + self.DoAction)
        method=getattr(self, DoAction, lambda :'Invalid')
        return method()


    # Do Actions
    def SendKeys(self):
        pyautogui.typewrite(self.DoParamX, interval=0.05)
        return [True,""]
    
    def Wait(self):
        sleep(int(self.DoParamX))
        return [True,""]
    
    def Click(self):
        pyautogui.click()
        return [True,""]
    
    def DoubleClick(self):
        pyautogui.doubleClick()
        sleep(1)
        return [True,""]
    
    def HotKeys(self):
        k = convertKey(self.DoParamX)
        if len(k) == 2:
            pyautogui.hotkey(k[0],k[1])
        return [True,""]
        
    def GetAttribute(self):
        text = self.element.get_attribute(self.DoParamX)
        if(text == self.DoParamY):
            return [True,""]
        else:
            return [False,"Actual Text found: " + util.xstr(text)]
    

    def pressEnter(self):
        pyautogui.press('enter')
        sleep(1)
        return [True,""]


    def Wait(self):
        sleep(self.DoParamX)
        return [True,""]
    
