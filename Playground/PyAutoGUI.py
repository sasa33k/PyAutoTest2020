'''
Created on Sep 28, 2019

@author: Sasa33k
Sasa33kHello world!Hello Hworld!
'''
import pyautogui
import subprocess

try:
    elem = pyautogui.locateCenterOnScreen('/Users/samantha/Dev/eclipse-workspace/autoTesting/logo.PNG', grayscale=True )
    print(elem)
    if subprocess.call("system_profiler SPDisplaysDataType | grep -i 'retina'", shell= True) == 0: 
        pyautogui.moveTo(elem[0]*0.5,elem[1]*0.5,3)
    else:
        pyautogui.moveTo(elem[0],elem[1],3)
    
except Exception as e:
    print(e)
    
pyautogui.click()
pyautogui.doubleClick()
pyautogui.hotkey('ctrl', 'c')
"""
pyautogui.moveRel(None, 10)
pyautogui.click()
pyautogui.hotkey('ctrl', 'v')
pyautogui.typewrite('Hello world!', interval=0.05)
pyautogui.press(['left', 'left', 'left', 'left', 'left', 'left'])
"""
"""
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
pyautogui.moveTo(100, 150)
pyautogui.click()
#  鼠标向下移动10像素
pyautogui.moveRel(None, 10)
pyautogui.doubleClick()
#  用缓动/渐变函数让鼠标2秒后移动到(500,500)位置
#  use tweening/easing function to move mouse over 2 seconds.
pyautogui.moveTo(1800, 500, duration=2, tween=pyautogui.easeInOutQuad)
#  在每次输入之间暂停0.25秒
pyautogui.typewrite('Hello world!', interval=0.25)
pyautogui.press('esc')
pyautogui.keyDown('shift')
pyautogui.press(['left', 'left', 'left', 'left', 'left', 'left'])
pyautogui.keyUp('shift')
pyautogui.hotkey('ctrl', 'c')
"""
