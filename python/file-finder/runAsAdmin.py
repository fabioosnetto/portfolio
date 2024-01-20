import ctypes
import sys

python_exe = sys.executable #get python interpreter
script     = './main.py' #script path to run as admin

ctypes.windll.shell32.ShellExecute32W(None, 'runas', python_exe, script, None, 1)