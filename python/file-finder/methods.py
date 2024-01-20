import os
import shutil
import interface

#--- Find File 
def findFile(tofind: str, init: str):
   """
   --> Find a file
   @params: tofind --> (string) file name to be found
   @params: init --> (string) path to init search
   @returns: path of file if was found, -1 if was not found
   """

   """
   file_name_to_find = tofind
   starting_directory = init

   for root, dirs, files in os.walk(starting_directory):
      if file_name_to_find in files:
         file_path = os.path.join(root, file_name_to_find)
         return file_path
   """

   try:
      path = init
      paths = os.listdir(path)

      _foundFile = findEqualValues(paths, tofind)
      if _foundFile:
         return path+_foundFile
      else:
         for p in paths:
            try:
               result = openNewPath(tofind, os.path.join(path, p))
            except:
               continue

            if result:
               return result
            else: 
               continue
         
         return
   except:
      return ''



#--- Find Equal String Values
def findEqualValues(values: str, checker: str):
   """
   ---> Check some value of values is equal to checker value
   @param values - lists of values to be checked
   @param checker - value to find in values
   @returns value equal checker = was found; '' = was not found
   """
   for v in values:
      if checker in v:
         return v
      
   return ''
      
#--- Open New Path
def openNewPath(tofind: str, init: str):
   """
   Recursive call 'findFile' method
   @params init - used to recursive calling of 'findFile' method
   @params tofind - used to recursive calling of 'findFile' method
   @returns findFile return
   """

   return findFile(tofind, init)


#--- Delete File on file path
def deleteFile(_file_path: str):
   """
   --> Delete _file_path
   @params: _file_path --> (string) define file to be deleted
   @returns: 0=success; -1=error 
   """

   try:
      if os.path.exists(_file_path):
         if os.path.isdir(_file_path):
            shutil.rmtree(_file_path)
         else:
            os.remove(_file_path)

         interface.success('[SUCCESS] File has been deleted')
         return 0
      else:
         interface.error('[ERROR] The file does not exist')
         return -1
   
   except PermissionError as err:
      interface.error('[ERROR] Access Denied. You probably do not have needed permissions')
      return -1
   

#--- Check end bar on path
def checkEndPathBar(path: str):
   """
   ---> Check if the path has a '/' at the end
   @params: path --> (string) path to be checked
   @returns: path with the end bar
   """
   
   if not (path[(len(path)-1)] == '/'):
      path = path+'/' 

   return path

