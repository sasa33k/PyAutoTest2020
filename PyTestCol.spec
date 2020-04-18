# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['PyAutoTest\\__main__.py'],
             pathex=['D:\\Pycharm-workspace\\PyAutoTest2020\\PyAutoTest', 'D:\\Pycharm-workspace\\PyAutoTest2020'],
             binaries=[('D:\\Pycharm-workspace\\PyAutoTest2020\\PyAutoTest\\resources\\win\\chromedriver.exe', '.\\PyAutoTest\\resources\\win')],
             datas=[('D:\\Pycharm-workspace\\PyAutoTest2020\\PyAutoTest\\Config.ini', '.\\PyAutoTest')],
             hiddenimports=['os', 'win32ctypes'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [('v', None, 'OPTION')],
          exclude_binaries=True,
          name='PyAutoTest',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='PyAutoTest')
