import PyAutoTest.common.runCaseUtil as runCaseUtil

'''
dirName = "D:\\"
fileName = "AutoTestTemplate"
osName = "win"

'''
dirName = "/Users/samantha/Dev/autotesting/"
fileName = "AutoTestTemplate"
osName = "mac"

### User Input
dirN = input('Folder [%s]' % dirName)
fileN = input('File Name [%s]' % fileName)
os = input('OS Name [win or %s]' % osName)
dirN = dirN or dirName
fileN = fileN or fileName
os = os or osName
print(dirN + "/" + fileN + ".xlsx")
runCaseUtil.run(dirN, fileN, os)