'''
Created on Sep 29, 2019

@author: Sasa33k

'''

import enum
import PyAutoTest.common.excelUtil as excelUtil
import PyAutoTest.common.commonUtil as util

class ActionType (enum.Enum):
    web = "web"
    win = "win"
    gui = "gui"
    
class Template (enum.Enum):
    sheets = ['ReadMe', 'RunConfig', 'Case', 'Steps']
    scenTitle = ['TestID', 'TestDescription', 'RepeatDataSheetName', 'CaseID']
    caseTitle = ['CaseID', 'CaseDescription', 'RepeatDataSheetName', 'Steps']
    stepTitle = ['StepID', 'StepDescription', 'ActionType', 'GetElement', 'GetParam', 'GetBy', 'Action', 'ActionParamX', 'ActionParamY', 'TakeScreenShot']
    getBy = ['Id','Name','Xpath', 'LinkText', 'PatialLinkText','TagName', 'ClassName', 'CssSelector']
    action = []
    
class Step(object):
    """A data descriptor that sets and returns values
       normally and prints a message logging their access.
    """
    def __init__(self, step):
        title = Template.stepTitle.value
        self.stepID = step.index(title[0])
        self.stepDesc = step.index(title[1])
        self.actionType = step.index(title[2])
        self.getElement = step.index(title[3])
        self.getParam = step.index(title[4])
        self.getBy = step.index(title[5])
        self.action = step.index(title[6])
        self.actionParamX = step.index(title[7])
        self.actionParamY = step.index(title[8])
        self.takeScreenshot = step.index(title[9])

    def __get__(self, obj, objtype):
        print('Retrieving', self.name)
        return self.val

    def __set__(self, obj, val):
        print('Updating', self.name)
        self.val = val
        
## Put Steps into Case steps

def CaseSteps(wb, testRec, case, addResult, offset=0):
    runArrRec = []
    #for case in testArr[1:]:
    tmpArrRec = []
    for item in case[3:]: # Steps in Case
        for step in testRec:
            if(step[0+offset] == item):
                currentStep = case[0:2] +step
                tmpArrRec.append(currentStep)
    #print(tmpArrRec)
    if(case[2]==None or case[2]==""):
        #print("--     NO REPEAT!! ")
        for step in tmpArrRec:
            if addResult:
                runArrRec.append([str(step[0])+"_0", None] + step)
            else:
                runArrRec.append(step)
    else:
        #print("--     REPEATING!! " + util.xstr(case[2])
        rDataSheet = excelUtil.dataSheet(wb, case[2])
        rData = excelUtil.dataRows(rDataSheet)
        rDataTitle = rData[0]
        for rec in rData[1:]:
            for step in tmpArrRec:
                tmp = step.copy() ## make a copy of original step for replacement
                for i in range(len(step)):
                    if util.xstr(step[i]).startswith("##"):
                        j=rDataTitle.index(step[i])
                        tmp[i] = rec[j]
                t=6
                if tmp[t+4] is not None and tmp[t+3] is not None:
                   pos = tmp[t+3].find("****")
                   tmp[t+3] = tmp[t+3][:pos]+tmp[t+4]+tmp[t+3][pos+4:]
                print(tmp)
                CaseRepeatID =  str(tmp[0]) +"_"+str(rec[0])
                if addResult:
                    runArrRec.append([CaseRepeatID, None] + tmp)
                else:
                    runArrRec.append(tmp)
    return runArrRec  
    print() 

