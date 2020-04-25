'''
Created on Sep 28, 2019

@author: Sasa33k

'''
import configparser, datetime
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
        dirName_default = config.get('INIT', 'dirName')
        resPath_default = config.get('INIT', 'resPath')

        if (reqInput == 'Y'):
            print('Use Default Config? [%(path)s, %(lv)s, %(res)s, %(dirN)s ]' % {'path':log_path_default, 'lv':log_level_default, 'res': resPath_default, 'dirN': dirName})
            defCon = input('type "N" for custom config: ')

        if (defCon == 'N'):
            log_path_input = input('Log Path [%s]: ' % log_path)
            log_level_input = input('Log Level [%s]: ' % log_level)
            resPath_input = input('Resource Path [%s]: ' % resPath)
            dirName_input = input('Test Folder Path [%s]: ' % dirName)
            log_path = log_path or log_path_input
            log_level = log_level or log_level_input
            resPath = resPath or resPath_input
            dirName = dirName or dirName_input
        else:
            log_path = log_path_default
            log_level = log_level_default
            dirName = dirName_default
            resPath = resPath_default


        fileName = config.get('INIT', 'fileName')
        osName = config.get('INIT', 'osName')
        reqInput = config.get('INIT', 'reqInput')

    except:
        print("Welcome to PyAutoTest")
        print("Error occur when getting default configs....")


    logger = Logger()
    logger.init(log_path, log_level)
    logger.info("")
    logger.info("---------")
    logger.info("PyAutoTest setup started...  ")
    logger.info("---------")


    if (reqInput == 'Y'):
        ### User Input
        file = input('File Name [%s]: ' % fileName)
        ps = input('OS Name [win or mac]: %s: ' % osName)
        file = file or fileName
        osn = ps or osName
        logger.info("App.RunCaseUtil By Input: " + dirName + file + '.xlsx')
        ##try:
        runCaseUtil.run(dirName, file, osn, logger, resPath)
        #except Exception as e:
        #    logger.error("App.RunCaseUtil: " + str(e))
        #    input('Press Enter to Exit... ')
    else:
        runCaseUtil.run(dirName, fileName, osName, logger, resPath)
        logger.info("App.RunCaseUtil Default: " + dirName + fileName + '.xlsx')
