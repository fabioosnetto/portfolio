import methods
import interface

def main():
   interface.fileFinderInterface()

   file = interface.reqFileToFind()
   initpath = interface.reqInitPath()
   print(methods.findFile(file, initpath))


main()