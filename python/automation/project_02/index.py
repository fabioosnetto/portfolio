import pyautogui
import requests
import pyperclip
from time import sleep

def main():
   sleep(2)
   login()
   pending = getPending()
   
   for i in range(0, pending):
      makeComm()
      sleep(2)
      markPoint()
      sleep(2)

   finish()


def getPosition():
   sleep(7)
   print(pyautogui.position())

def login():
   pyautogui.PAUSE = 2

   # open navigator
   pyautogui.moveTo(x=1258, y=11)
   pyautogui.click()
   pyautogui.write('chrome')
   pyautogui.press('enter')

   # open new tab
   pyautogui.hotkey('command', 't')

   # connect with website
   url = 'https://portal.yousenior.com.br:4443/login'
   if(testWebConn(url)): 
      pyautogui.write(url)

      pyautogui.PAUSE = 5

      pyautogui.press('enter')
   else:
      return
  
   # login
   pyautogui.press('tab', presses=3)
   pyautogui.press('enter')
   
def getPending():
   pyautogui.PAUSE = 0.5

   pyautogui.moveTo(x=464, y=529)
   pyautogui.click()
   pyautogui.rightClick()
   pyautogui.hotkey('command', 'c')
   pending = int(str(pyperclip.paste()).split('Pendentes (')[1].split(')')[0])

   return pending if str(pending).isnumeric else 1

def makeComm():
   pyautogui.PAUSE = .4

   pyautogui.click(x=1231, y=625)
   pyautogui.press('tab')
   pyautogui.write('home office')
   pyautogui.press('enter')
   pyautogui.press('esc')
   pyautogui.PAUSE = 0.5

def markPoint():
   pyautogui.PAUSE = 0.5

   pyautogui.moveTo(x=323, y=646)
   pyautogui.rightClick()
   pyautogui.hotkey('command', 'c')
   day      = pyperclip.paste()
   end_time = str('17:00' if day == 'sexta' else '18:00')  


   pyautogui.moveTo(x=576, y=629)
   pyautogui.click()
   pyautogui.moveTo(x=325, y=424)
   pyautogui.click(clicks=4)
   
   pyautogui.press('tab', presses=12)
   pyautogui.write('08:00')
   pyautogui.press('tab', presses=2)
   pyautogui.write('7')
   pyautogui.press('enter')
   pyautogui.press('tab', presses=2)

   pyautogui.write('12:00')
   pyautogui.press('tab', presses=2)
   pyautogui.write('7')
   pyautogui.press('enter')
   pyautogui.press('tab', presses=2)

   pyautogui.write('13:00')
   pyautogui.press('tab', presses=2)
   pyautogui.write('7')
   pyautogui.press('enter')
   pyautogui.press('tab', presses=2)

   pyautogui.write(end_time)
   pyautogui.press('tab', presses=2)
   pyautogui.write('7')
   pyautogui.press('enter')
   pyautogui.press('tab', presses=2)
   pyautogui.press('enter')
   pyautogui.PAUSE = 2.5

def testWebConn(url: str):
   """
   Test connection with a website
   @param: url (string) - website url
   @returns: boolean - true: connection ok; false: connection issue
   """

   try:
      resp = requests.get(url)
      if(resp.status_code == 200):
         print(f'Website {url} is reachable with status code 200!')
         return True
      else: 
         print(f'Website {url} is reachable but status code is {resp.status_code}!')
   except:   
      print(f'Website {url} is not reachable')
   
   return False

def finish():
   print('Congratulations, your work hours are up to date.')
   print('Clocked in by pyautogui!')

   pyautogui.hotkey('command', 't')
   pyautogui.write('Congratulations, your work hours are up to date.')

main()
