# import sys
# import os
# import tkinter
# import PIL
# from cx_Freeze import setup, Executable
#
#
# # Dependencies are automatically detected, but it might need fine tuning.
# build_exe_options = {"packages": ["os","sys"], "excludes": ["tkinter","PIL","tkinter.ttk","tkinter.filedialog"]}
#
# # GUI applications require a different base on Windows (the default is for a
# # console application).
# base = None
# if sys.platform == "win32":
#     base = "Win32GUI"
#
# executables = {
#     Executable("fanyi.py", base=base)
# }
# setup(  name = "guifoo",
#         version = "0.1",
#         description = "My GUI application!",
#         options = {"build_exe": build_exe_options},
#         executables = executables)

import sys
import os
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = r'C:\Users\Liu\Anaconda3\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Liu\Anaconda3\tcl\tk8.6'

include_files = {
    r"C:\Users\Liu\Anaconda3\DLLs\tcl86t.dll",
    r"C:\Users\Liu\Anaconda3\DLLs\tk86t.dll"
}

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = {
    Executable('fanyi.py',base=base)
}

packages = []

setup(
    name = "测试1.0",
    version = "1.0",
    description = 'test',
    executables = executables
)