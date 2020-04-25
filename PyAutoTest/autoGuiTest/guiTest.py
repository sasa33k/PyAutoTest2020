'''
Created on Sep 29, 2019

@author: Sasa33k

'''

from PyAutoTest.common import commonUtil as util
from PyAutoTest.autoGuiTest import getClass, actionClass
from PyAutoTest.data.enumTemplate import Template
from time import sleep
import pyautogui



def ProcessStep(resolutionFactor, logger, step, t, saveDir,seq="", caseID=0, dirName='.'):
    element = None
    screenName = str(seq)+"_"+str(caseID)+"_"+ str(step[t.stepID])
    screenPath = saveDir+screenName
    logger.info("    ... " + str(step) + " | " + util.xstr(step[t.getElement]) + " . " + util.xstr(step[t.action]))
    # Get Something if step[3] GetElement not empty
    if(step[t.getElement]!="" and step[t.getElement]!=None):
        #element = Get(browser)
        getParam = step[t.getElement]
        getMethod = step[t.getBy]
        g=getClass.Switcher()
        
        #element = g.Get(getParam, getMethod)
        
        try:
            element = g.Get(logger, resolutionFactor, getParam, getMethod, dirName)
        except Exception as e:
            logger.error("*** EXCEPTION: " + str(e))
            logger.error("Get Exception occur")
            pyautogui.screenshot(screenPath + "_getException.png");
            return ['=HYPERLINK(".\\' +screenName+'_getException.png","getException")', False, "Get Exception occurs: "+str(e)]
        
        logger.info("--")
        logger.info(element)
        logger.info(type(element))
        logger.info("--")
    # check if element NOT exist (returned string) = failed
    if(isinstance(element, str) and step[t.action] != "Wait" ):
        result = ['=HYPERLINK(".\\' +screenName+'_getException.png","getException")',False, element]
        return result
    # Do Something if step[5] Action not empty
    elif(step[t.action]!="" and step[t.action]!=None):
        DoAction = step[t.action]
        DoParamX = step[t.actionParamX]
        DoParamY = step[t.actionParamY]
        s=actionClass.Switcher()
        try:
            result = s.Do(logger, element, DoAction, DoParamX, DoParamY)
            #print(screenPath + "_DoException.png")
        
        except Exception as e:
            logger.error("Action Exception occur: " + str(e))
            pyautogui.screenshot(screenPath + "_DoException.png");
            return ['=HYPERLINK(".\\' +screenName+'_DoException.png","doException")', False, "Action Exception occurs"]
        
    screenLink=[""]

    # take screenshots
    if(step[t.takeScreenshot]=="Yes"):
        sleep(2)
        pyautogui.screenshot(screenPath + "_screenshot.png");
        screenLink = ['=HYPERLINK(".\\' +screenName+'_screenshot.png","screenshot")']

    return screenLink + result

