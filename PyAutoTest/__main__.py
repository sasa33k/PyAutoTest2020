'''
Created on Sep 28, 2019

@author: Sasa33k
pywin32_postinstall.py -install
pyinstaller --clean --debug=all --hidden-import pywin32-ctypes --hidden-import pywin32 --noupx --onefile PyAutoTest.py
pyinstaller PyTest.spec PyAutoTest\__main__.py

'''
from PyAutoTest import app

if __name__ == '__main__':
# def main():
    app.run()
