'''
Created on Oct 17, 2019

@author: n0321235
'''
from PyAutoTest.common.logUtil import Logger
import configparser


def AddOrReplace(arr, key, value):
    isExist = False
    for i in range(len(arr)):
        if arr[i][0] == key:
            arr[i] = (key, value)
            isExist = True
    if not isExist:
       arr.append((key, value))

    print(arr)


a = []
a.append(("aaa", "111"))
a.append(("bbb", "111"))
AddOrReplace(a, "aaa", "222")
k = input('key: ')
v = input('value: ')
AddOrReplace(a, k, v)

'''
config = configparser.ConfigParser()
config.read('../Config.ini')
path = config.get('LOGGER', 'path')
level = config.get('LOGGER', 'level')
print ('section_a_Value = ', path )
print ('section_b_Value = ', level )

logger = Logger()
logger.init(path,level)

#logger.debug("debug message")
logger.info("something info")
 
'''
