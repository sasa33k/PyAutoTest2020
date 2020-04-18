
from cx_Freeze import setup, Executable
 
 # setup(
 #   name = "PyAutoTest" ,
 #   version = "0.1" ,
 #   description = "Test with PyAutoTest!" ,
 #   executables = [Executable("__main__.py")] ,
 #   )

#buildOptions = dict(include_files = [(absolute_path_to_your_file,'final_filename')]) #single file, absolute path.
"""
buildOptions = dict(include_files = ['D:\eclipse-workspace\PyAutoTest\PyAutoTest']) #folder,relative path. Use tuple like in the single file to set a absolute path.

setup(
    name = "PyAutoTest" ,
    version = "0.1" ,
    description = "Test with PyAutoTest!" ,
    author = "Sasa33k",
    options = dict(build_exe = buildOptions),
    executables = [Executable("app.py")]
    )
"""
import sys

from cx_Freeze import setup, Executable

#build_exe_options = {'icon': 'chkimg.ico', 'include_files': ['chkimg.ico', 'folder.gif'], 'packages':['lxml']}
build_exe_options = dict(include_files = ['D:\eclipse-workspace\PyAutoTest\PyAutoTest'])

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executable = Executable('AppTest.py', base=base)

setup(
        name = "PyAutoTest" ,
        version = "0.1" ,
        description = "Test with PyAutoTest!" ,
        author = "Sasa33k",
        options = {'build_exe': build_exe_options},
        executables = [executable])