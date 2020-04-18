'''
Created on Oct 1, 2019

@author: Sasa33k

'''
from PyAutoTest.data.enumTemplate import Template

TestStepsTitle=['StepDescription', 'ActionType', 'GetElement', 'GetBy', 'Action', 'ActionParamX','StepID',  'ActionParamY', 'TakeScreenShot']
s=Template(TestStepsTitle)
print(s.stepID)
print(s.stepDesc)
