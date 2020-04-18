'''
Created on Sep 29, 2019

@author: Sasa33k

'''
def xstr(s):
    if s is None:
        return ''
    return str(s)

def AddOrReplace(arr, key, value):
    isExist = False
    for i in range(len(arr)):
        if arr[i][0] == key:
            arr[i] = (key, value)
            isExist = True
    if not isExist:
       arr.append((key, value))


def getParam(arr, key):
    isExist = False
    for i in range(len(arr)):
        if arr[i][0] == key:
            isExist = True
            return arr[i][1]
    if not isExist:
        return None
