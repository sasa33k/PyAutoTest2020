import os, _ctypes, ctypes

import PyInstaller.__main__
PyInstaller.__main__.run([
    '--name=main',
    '--clean',
    '--paths=D:\Pycharm-workspace\PyAutoTest2020\PyAutoTest',
    '--add-data=D:\Pycharm-workspace\PyAutoTest2020\PyAutoTest\Config.ini;.',
    '--add-binary=D:\Pycharm-workspace\PyAutoTest2020\PyAutoTest\resources\win\chromedriver.exe;.',
    '--debug=imports',
    #'--onefile',
    '--console',
    '--hiddenimport=os',
    '--hiddenimport=win32ctypes',
    #'--add-binary=pywin32-ctypes',
    os.path.join('PyAutoTest','__main__.py')
])