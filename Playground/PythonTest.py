'''
Created on Sep 28, 2019

@author: Sasa33k

'''
Steps = [
    [1,"Fetch Page", "aa","a11"],
    [2,"Do Something", "bb","222"],
    [3,"Do Again", "cc","cccc"],
    [5,"Do 55", "bb","222"],
    [6,"Do 66", "cc","cccc"]
]
StepNo = [1,2,3,5,6]

CaseStepNo = [5,3, 2, 3]


for num in CaseStepNo:
    print(str(Steps[StepNo.index(num)][0]) + " : " + Steps[StepNo.index(num)][1])

    
print("---")

## While loop
i = 1
while i <= len(StepNo):
    i+=1