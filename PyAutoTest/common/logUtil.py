'''
Created on Oct 17, 2019

@author: Sasa33k
'''
import logging

class Logger(object):
    # Setup Get functions
    def init(self, file, level):
        logging.basicConfig(filename=file,
                    format='%(asctime)-24s: %(levelname)-8s: %(message)s')
    #                ,datefmt='%Y-%m-%d %H:%M:%S %p')
        self.logger=logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        
        #return logger
    
    def info(self, msg):
        print("-INFO: ",msg)
        self.logger.info(msg)

    def debug(self, msg):
        print("-DEBUG: ",msg)
        self.logger.debug(msg)
        
    def warning(self, msg):
        print("*WARN: ",msg)
        self.logger.warning(msg)
        
    def critical(self, msg):
        print("**CRITICAL: ",msg)
        self.logger.critical(msg)
        
    def error(self, msg):
        print("***ERROR: ",msg)
        self.logger.error(msg)