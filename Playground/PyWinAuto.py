'''
Created on Sep 27, 2019

@author: Sasa33k

'''
from pywinauto.application import Application, findbestmatch
import  time
app = Application(backend="uia").start('notepad.exe') 
#dlg_spec = app.UntitledNotepad
#wait for window available
actionWin = app[' Untitled - Notepad ']
actionWin.wait('ready', timeout=5, retry_interval=3)
#app.UntitledNotepad.wait('visible')




actionWin.Edit.type_keys("Hi from Python interactive prompt %s" % str(dir()), with_spaces = True)
actionWin.menu_select("File -> Save")

time.sleep(1)
actionWin["Save As"].type_keys("cccc.txt")
#actionWin.Edit.type_keys("abc.txt")

actionWin.Save.click()
#actionWin["Save As"].ConfirmSaveAs.Yes.click()
# If file exists - it asks you if you want to overwrite
try:
    actionWin["Save As"].ConfirmSaveAs.Yes.wait('exists').click()
except findbestmatch.MatchError:
    print('Skip overwriting...')

time.sleep(1)
app.window(best_match='Notepad').menu_select("File->Exit")
    # exit notepad
#app.actionWin.menu_select("File->Exit")

