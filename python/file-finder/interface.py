import os
from time import sleep
import methods

#--- Start File Finder Interface
def fileFinderInterface():
   os.system('cls')

   drawLine(10)
   title = 'File Finder'.center(28)
   print(f'+{toRed(title)}+')
   drawLine(10)
   print(toRed("This is a development version. Some functionalities can't work as expected.\n"))

#--- Request file name to be found
def reqFileToFind():
   """
   ---> Request User the file name to be found
   @returns: file name
   """
   file = input(toPurple('\nWrite a keyword to be found')+' (if more than one, separe by a single whitespace):\n')
   file = file.strip()
   
   return file

#--- Request Init path to start finder
def reqInitPath():
   """
   ---> Request User the init path for begin searches
   @returns: init path
   """
   
   default = reqDefInitPath()

   init_path = '-1'
   valid_resp = init_path == '1' or init_path == '2' or init_path == '3'
   
   while not valid_resp:
      init_path = input(
         f'\n{toPurple("Choose the init path to start the File Finder:")}\n'
         f'{toBlue("[1]")} Default ({default})\n'
         f'{toRed("[2]")} Other Path\n'
         f'{toPurple("[3]")} Edit Default path\n'
      )

      init_path = init_path.strip()
      valid_resp = init_path == '1' or init_path == '2' or init_path == '3'

      if not valid_resp:
         error('Please, enter a valid option', 3)
   
   if init_path == '1':
      return init_path
   
   elif init_path == '2':
      init_path = input(toPurple('\nPlease, enter the initialization path:\n'))
      init_path = init_path.strip()
      init_path = methods.checkEndPathBar(init_path)
      return init_path

   elif init_path == '3':
      editDefInitPath()
      reqInitPath()

#--- Request Default Path
def reqDefInitPath():
   """
   ---> Request Default Initialization Path defined
   @returns: default path
   """
   with open('C:/Users/ADM/OneDrive/Área de Trabalho/Fabio-Data/coding/my/portfolio/python/file-finder/data/default_path.txt', 'rt') as default:
      return default.read()

#--- Redefine Default Path
def editDefInitPath():
   """
   ---> Edit Default Initialization Path defined
   @returns: 0=edited with success; -1=cannot edit
   """

   new_path = input(toPurple('\nPlease, enter the new default path:'))
   new_path = new_path.strip()
   new_path = methods.checkEndPathBar(new_path)

   try:
      with open('C:/Users/ADM/OneDrive/Área de Trabalho/Fabio-Data/coding/my/portfolio/python/file-finder/data/default_path.txt', 'wt') as default:
         default.write(new_path)

   except KeyError as err:
      error('[ERROR] Cannot overwrite default path < '+err+' >')
      return -1
   finally:
      success('[SUCCESS] Default Path Edited!')
      return 0


#--- Send an Error messange
def error(err: str, sleep_time: int = 5):
   """
   ---> Send an error message and wait a time
   @params: err --> (string) message to display
   @params: sleep_time --> (integer > 0) timer for message
   @returns: without return
   """

   print(f'\n{toRed(err)}\n')
   print('Continuing after: \n')
   
   if sleep_time<0:
      sleep_time = 5
      
   for s in range(sleep_time, -1, -1):
      print(s, end='  ', flush=True)
      sleep(1)

#--- Send a Success message
def success(msg: str, sleep_time: int = 5):
   """
   ---> Send an succes message and wait a time
   @params: msg --> (string) message to display
   @params: sleep_time --> (integer > 0) timer for message
   @returns: without return
   """

   print(f'\n{toBlue(msg)}\n')
   print('Continuing after: \n')
   
   sleep_time = 5 if sleep_time<0 else ''
   for s in range(sleep_time, -1, -1):
      print(s, end='  ', flush=True)
      sleep(1)

#--- Draw a Division Line
def drawLine(width: int, color: str = '\033[m'):
   """
   ---> Draw a Division Line at width
   @params: width --> (integer) line width
   @returns: no return
   """
   print(f'{color}-=-\033[m'* width)


#--- Text to Red
def toRed(txt: str):
   """
   ---> Turn text to red
   @params: txt --> (string) text to turn red
   @returns: modified text
   """
   return f'\033[31m{txt}\033[m'
#--- Text to Blue
def toBlue(txt: str):
   """
   ---> Turn text to blue
   @params: txt --> (string) text to turn blue
   @returns: modified text
   """
   return f'\033[36m{txt}\033[m'
#--- Text to Purple
def toPurple(txt: str):
   """
   ---> Turn text to purple
   @params: txt --> (string) text to turn purple
   @returns: modified text
   """
   return f'\033[34m{txt}\033[m'