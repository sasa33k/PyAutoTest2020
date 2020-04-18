'''
Created on Sep 28, 2019

@author: Sasa33k

'''
import configparser
import sys, os

import PyAutoTest.common.runCaseUtil as runCaseUtil
from PyAutoTest.common.logUtil import Logger


def resource_path(relative_path):
    base_path = os.path.dirname(__file__)
    return os.path.join(os.path.dirname(base_path), relative_path)


def run():
    BASE_DIR = os.path.abspath(resource_path(os.path.join('PyAutoTest', 'Config.ini')))
    config = configparser.RawConfigParser()
    config.read(BASE_DIR)

    log_path = os.path.join(os.path.dirname(os.path.dirname(sys.executable)), 'debug.log')
    log_level = 'DEBUG'

    dirName = os.path.join(os.path.dirname(os.path.dirname(sys.executable)), 'AutoTesting')
    resPath = os.path.join(os.path.dirname(os.path.dirname(sys.executable)), 'AutoTesting', 'resources')
    fileName = 'AutoTestTemplate'
    osName = 'mac'
    reqInput = 'Y'

    try:
        ver = config.get('VERSION', 'Version')
        print("Welcome to PyAutoTest", ver)
        print("-----")
        log_path_default = config.get('LOGGER', 'path')
        log_level_default = config.get('LOGGER', 'level')
        resPath_default = config.get('INIT', 'resPath')

        if (reqInput == 'Y'):
            print('Use Default Config? [%(path)s, %(lv)s, %(res)s]' % {'path':log_path_default, 'lv':log_level_default, 'res': resPath_default})
            defCon = input('type "N" for custom config')

        if (defCon == 'N'):
            log_path_input = input('Log Path [%s]' % log_path)
            log_level_input = input('Log Level [%s]' % log_level)
            resPath_input = input('Resource Path [%s]' % resPath)
            log_path = log_path or log_path_input
            log_level = log_level or log_level_input
            resPath = resPath or resPath_input
        else:
            log_path = log_path_default
            log_level = log_level_default

        dirName = config.get('INIT', 'dirName')
        fileName = config.get('INIT', 'fileName')
        osName = config.get('INIT', 'osName')
        reqInput = config.get('INIT', 'reqInput')
        resPath = config.get('INIT', 'resPath')
    except:
        print("Welcome to PyAutoTest")

    logger = Logger()
    logger.init(log_path, log_level)

    if (reqInput == 'Y'):
        ### User Input
        dir = input('Test Folder [%s]' % dirName)
        file = input('File Name [%s]' % fileName)
        ps = input('OS Name [win or mac]: %s' % osName)
        dir = dir or dirName
        file = file or fileName
        osn = ps or osName
        print(dir + file + '.xlsx')
        runCaseUtil.run(dir, file, osn, logger, resPath)
    else:
        runCaseUtil.run(dirName, fileName, osName, logger, resPath)
        print(dirName + fileName + '.xlsx')
