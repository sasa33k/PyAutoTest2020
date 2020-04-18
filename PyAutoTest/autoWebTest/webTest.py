'''
Created on Sep 29, 2019

@author: Sasa33k

'''

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException
from PyAutoTest.autoWebTest import actionClass, getClass
from PyAutoTest.common import commonUtil as util
import PyAutoTest.common.GlobalParam as gp
import os.path

def resource_path(relative_path):
    try:
        base = sys._MEIPASS
        base_path = os.path.dirname(base)
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(os.path.dirname(base_path), relative_path)


def Init(arg, osName, resPath):
    print(resPath)
    print(os.path.dirname(__file__))
    options = webdriver.ChromeOptions()
    base_path = os.path.dirname(__file__)
    if (arg == "headless"):
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
    if(osName == "mac"):
        print("XXX")
        #driverlink = parentDir + '/resources/mac/chromedriver'
        #print(driverlink)
        #browser = webdriver.Chrome(executable_path=driverlink, chrome_options=options)
        #browser = webdriver.Chrome(resource_path('resources/mac/chromedriver'), chrome_options=options)
        print(os.path.join(resPath, 'mac', 'chromedriver'))
        browser = webdriver.Chrome(os.path.join(resPath, 'mac', 'chromedriver'), chrome_options=options)
    else:
        print(resource_path('resources\\win\\chromedriver.exe'))
        #browser = webdriver.Chrome(parentDir + '/resources/win/chromedriver.exe', chrome_options=options)
        browser = webdriver.Chrome(resource_path('resources\\win\\chromedriver.exe'), chrome_options=options)
    return browser

def InitialWin(browser):
    return browser.current_window_handle;

def ProcessStep(browser, step, t, saveDir,seq="", caseID=0, initialWin=None):

    element = None
    screenName = seq+"_"+str(caseID)+"_"+ str(step[t.stepID])
    screenPath = saveDir+screenName
    print("    ... " + str(step) + " | " + util.xstr(step[t.getElement]) + " . " + util.xstr(step[t.action]))
    # Get Something if step[3] GetElement not empty
    if(step[t.getElement]!="" and step[t.getElement]!=None):
        #element = Get(browser)
        getParam = step[t.getElement]
        getMethod = step[t.getBy]
        g=getClass.Switcher()
        
        try:
            element = g.Get(browser, getParam, getMethod, initialWin)
            print(screenPath + "_getException.png")
        
        except TimeoutException:
            print("Timeout: element not found")
            browser.save_screenshot(screenPath + "_getException.png");
            return ['=HYPERLINK(".\\' +screenName+'_getException.png","getException")', False, "Timeout: element not found"]
        
        except:
            print("Get Exception occur")
            browser.save_screenshot(screenPath + "_getException.png");
            return ['=HYPERLINK(".\\' +screenName+'_getException.png","getException")', False, "Get Exception occurs"]
        
    # check if element NOT exist (returned string) = failed
    if(isinstance(element, str) and step[t.action] != "Wait" ):
        result = [False, element]
    # Do Something if step[5] Action not empty
    elif(step[t.action]!="" and step[t.action]!=None):
        DoAction = step[t.action]
        DoParamX = step[t.actionParamX]
        DoParamY = step[t.actionParamY]
        s=actionClass.Switcher()
        try:
            result = s.Do(browser, element, DoAction, DoParamX, DoParamY)
            print(screenPath + "_DoException.png")
        
        except ElementNotInteractableException:
            print("Timeout: element not interactable")
            browser.save_screenshot(screenPath + "_DoException.png");
            return ['=HYPERLINK(".\\' +screenName+'_DoException.png","doException")', False, "Timeout: element not interactable"]
        '''
        except:
            print("Action Exception occur")
            browser.save_screenshot(screenPath + "_DoException.png");
            return ['=HYPERLINK(".\\' +screenName+'_DoException.png","doException")', False, "Action Exception occurs"]
        '''
    screenLink=[""]
    # take screenshots
    if(step[t.takeScreenshot]=="Yes"):
        browser.implicitly_wait(2)
        browser.save_screenshot(screenPath + "_screenshot.png");
        screenLink = ['=HYPERLINK(".\\' +screenName+'_screenshot.png","screenshot")']
    return screenLink + result

def Quit(browser):
    browser.quit()

"""   
browser.get('http://www.yahoo.com')
assert 'Yahoo' in browser.title
"""