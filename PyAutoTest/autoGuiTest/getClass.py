'''
Created on Sep 29, 2019

@author: Sasa33k

'''
import pyautogui, os
from time import sleep

def convertPos(txtPos):
    posSplit = txtPos.split(',')
    if( len(posSplit) >= 2):
        posArr=[]
        for item in posSplit:
            try:
                posArr.append(int(item))
            except:
                posArr.append(None)
            
        return posArr
    else:
        return [None, None]


class Switcher(object):
    # Setup Get functions
    def Get(self, resolutionFactor=1, getParam = None, getMethod = None, dirName = '.'):
        self.speed = 0.1
        self.resol = resolutionFactor
        self.getMethod = getMethod
        self.getParam = getParam
        self.dirName = dirName
        print("    ... Locating: " + getParam + " By " + getMethod)
        
        
        method=getattr(self, "By"+getMethod, lambda :'Invalid')
        return method()
        
    
    # Get By Actions
    def ByImg(self):
        print(self.getParam)
        imgPath = os.path.join(self.dirName, 'img', self.getParam)
        print(imgPath)
        numRepeat = 1
        elemPos = None

        # Retry 3 Times
        error=''
        while (elemPos == None) and (numRepeat > 0):
            print("Getting element: repeat " + str(numRepeat))
            try:
                elemPos = pyautogui.locateCenterOnScreen(imgPath)
            except Exception as e:
                error=str(e)
                print(e)
                sleep(3)
            numRepeat -= 1
        
        
        if (elemPos == None):
            return "getException occurs: " + error
        else:
            pyautogui.moveTo(elemPos[0]*self.resol, elemPos[1]*self.resol, 1)
            return elemPos
    
    def ByPos(self):
            
            elemPos = convertPos(self.getParam)
            if all(elemPos):
                pyautogui.moveTo(elemPos[0]*self.resol,elemPos[1]*self.resol,1)
            else:
                pyautogui.moveRel(elemPos[0]*self.resol,elemPos[1]*self.resol,1)
            print("moved to: " + str(elemPos))
            
            return elemPos
     
    def ByRelPos(self):
            
            elemPos = convertPos(self.getParam)
            pyautogui.moveRel(elemPos[0]*self.resol,elemPos[1]*self.resol,1)
            print("moved relatively: " + str(elemPos))
            
            return elemPos   
        
    