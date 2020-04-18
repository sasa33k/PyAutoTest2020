'''
Created on Sep 29, 2019
 set the default encoding for Eclipse to utf-8 (which is usually the default platform encoding) -- 
 you can do this at Window > preferences > general > workspace.
@author: Sasa33k

'''
import os
import subprocess
from datetime import datetime

import PyAutoTest.autoGuiTest.guiTest as guiTest
import PyAutoTest.autoWebTest.webTest as webTest
import PyAutoTest.data.enumTemplate as AT
import PyAutoTest.common.GlobalParam as gp
from PyAutoTest.common import commonUtil as util
from PyAutoTest.common import excelUtil
from PyAutoTest.data.enumTemplate import Template, ActionType, Step, CaseSteps


def run(dirName, fileName, osName, logger, resPath):
    # fileName = "AutoTestGUI"

    ### File Directory setup
    beginTime = datetime.now()
    beginTimeStr = beginTime.strftime("%Y%m%d%H%M")

    readPath = dirName + "/" + fileName + ".xlsx"
    saveResultDir = dirName + "/Results/"
    saveDir = saveResultDir + fileName + "_" + beginTimeStr
    savePath = saveDir + "/_" + fileName + "_" + beginTimeStr + "_Result.xlsx"
    resolutionFactor = 1

    ## check if display is retina for mac
    if subprocess.call("system_profiler SPDisplaysDataType | grep -i 'retina'", shell=True) == 0:
        resolutionFactor = 0.5


    ### Load Test Template file
    wb = excelUtil.load(readPath)
    sheetNames = wb.sheetnames

    ## Check if valid sheets get sheets
    validSheets = excelUtil.validateTitle(Template.sheets.value, sheetNames)
    configSheet = excelUtil.dataSheet(wb, "RunConfig")
    caseSheet = excelUtil.dataSheet(wb, "Case")
    dataSheet = excelUtil.dataSheet(wb, "Steps")

    ## get data rows list
    testScenarios = excelUtil.dataRows(configSheet)
    testCases = excelUtil.dataRows(caseSheet)
    testSteps = excelUtil.dataRows(dataSheet)

    ## Process data
    scenTitle = testScenarios[0][3:5]

    caseTitle = testCases[0][0:2]
    stepTitle = testSteps[0]
    finalTitle = scenTitle + ['CaseRepeatID', 'CaseResult'] + caseTitle + stepTitle + ['Screenshot', 'Result',
                                                                                       'Message']

    containWebTest = excelUtil.containElement(ActionType.web.value, dataSheet['C'])
    validStepTitle = excelUtil.validateTitle(Template.stepTitle.value, stepTitle)

    logger.info(finalTitle)
    print()

    runCaseSteps = []
    for i in range(len(testCases) - 1):
        runCaseSteps += CaseSteps(wb, testSteps[1:], testCases[i + 1], True)
        print(CaseSteps(wb, testSteps[1:], testCases[i + 1], True))
    print()
    finalSummary = []
    finalSummary.append(["Start Time: " + datetime.now().strftime("%d-%b-%Y, %H:%M:%S")])
    finalSummary.append(["Test Name", "Final Result"])
    finalResultData = []
    ### Title valid, proceed with testing
    if (validStepTitle):

        ## Create directory for result file and screenshots
        print("Creating Directory")
        if not os.path.exists(saveResultDir):
            os.mkdir(saveResultDir)
            logger.info("Directory " + saveResultDir + " Created ")
        else:
            logger.info("Directory " + saveResultDir + " already exists")

        if not os.path.exists(saveDir):
            os.mkdir(saveDir)
            logger.info("Directory " + saveDir + " Created ")
        else:
            logger.info("Directory " + saveDir + " already exists")

        print()

        for i in range(len(testScenarios) - 1):
            isRun = testScenarios[i + 1][0]
            param = testScenarios[i + 1][2]
            testId = testScenarios[i + 1][3]
            print(testScenarios)
            testName = str(testId) + "_" + testScenarios[i + 1][4]
            if (isRun == "Yes"):
                print()
                print("********************")
                print("Running for test: " + testName)
                runTestSteps = CaseSteps(wb, runCaseSteps, testScenarios[i + 1][3:], False, 2)

                print()

                for s in runTestSteps:
                    print(s)

                print("********************")

                ## Process Test Steps
                print("Processing Test Steps in Case X ...")
                print(finalTitle)
                t = Step(finalTitle)
                # ** IF have web test
                if (containWebTest):
                    print(".. Include web tests")
                    browser = webTest.Init(param, osName, resPath)
                    initialWin = webTest.InitialWin(browser)
                    browser.maximize_window()

                # set up data & title
                stepResults = []
                caseResult = []
                resultData = []
                caseInfo = [testName, None, "Start Time: " + datetime.now().strftime("%d-%b-%Y, %H:%M:%S"), None]
                resultData.append(caseInfo)
                resultData.append(["Seq"] + finalTitle[2:])
                finalResult = ""

                # Process each step in case
                seq = 0
                startSeq = 1
                prevCaseRepeatID = ""
                for step in runTestSteps:
                    seq += 1
                    seqName = "T" + str(testId) + "S" + str(seq)

                    # handle getting param with prefix __
                    tmpStep = []
                    for param in step:
                        if util.xstr(param).startswith("__"):
                            param = util.getParam(gp.savedParam, util.xstr(param[2:]))
                        tmpStep.append(param)
                    step = tmpStep
                    result = []

                    print(step)
                    ## Selenium web browser teststep
                    if (step[t.actionType] == AT.ActionType.web.value):
                        print("    Web | " + str(step[t.stepID]) + " : " + util.xstr(step[t.stepDesc]) + util.xstr(
                            step[t.getElement]))
                        result = webTest.ProcessStep(browser, step, t, saveDir + "/", seqName, step[2],
                                                     initialWin)  # 0: testID, 2: caseID
                        print(gp.savedParam)

                        print("    >>> " + str(result))

                    ## PyWinAuto windows application teststep
                    elif (step[t.actionType] == AT.ActionType.win.value):
                        print("    Win | " + str(step[t.stepID]) + " : " + step[t.stepDesc])
                        # webTest.ProcessStep(browser, step, t, saveDir+"/", seqName, step[2]) # 0: testID, 2: caseID
                        result = [None, None, "WIP"]
                    ## PyAutoGUI GUI teststep
                    elif (step[t.actionType] == AT.ActionType.gui.value):
                        print("    GUI | " + str(step[t.stepID]) + " : " + step[t.stepDesc])
                        result = guiTest.ProcessStep(resolutionFactor, step, t, saveDir + "/", seqName,
                                                     step[2], dirName)  # 0: testID, 2: caseID


                    else:
                        print("XXXXXXX " + str(t.actionType))
                        result = [None, False, "No Action Matched"]

                    resultData.append([seq] + step[2:] + result)

                    if (prevCaseRepeatID == step[2]):
                        stepResults.append(result[1])

                    else:
                        print("~~ " + prevCaseRepeatID + step[2])
                        caseResult.append(all(stepResults))
                        while startSeq < seq:
                            resultData[startSeq + 1][2] = all(stepResults)
                            print(str(startSeq) + str(all(stepResults)))
                            startSeq += 1

                        stepResults = []
                        stepResults.append(result[1])

                    prevCaseRepeatID = step[2]

                    finalResult = str(all(caseResult))

                caseInfo.append("End Time: " + datetime.now().strftime("%d-%b-%Y, %H:%M:%S"))
                caseInfo.append(None)
                caseInfo.append("Final Result: " + finalResult)
                finalResultData.append(resultData)
                finalSummary.append([testName, finalResult])

                # ** IF have web test
                if (containWebTest):
                    browser = webTest.Quit(browser)

                print()
                print("Total " + str(seq) + " steps executed")
            else:
                print("--- Skip Test " + testName)
    else:
        print("Template not valid. ")

    #### Write result data
    for s in finalResultData:
        print(s)
        for i in s:
            print(" ... " + str(i))
    print(" ... ")
    for s in finalSummary:
        print(s)
    print(" ... ")

    finalSummary[0].append("End Time: " + datetime.now().strftime("%d-%b-%Y, %H:%M:%S"))
    if (len(finalResultData) > 0):
        try:
            excelUtil.write(finalSummary, finalResultData, savePath)
            print("Test Completed!")
        except:
            print("Error in Writing Excel")
