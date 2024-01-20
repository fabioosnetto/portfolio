import pyautogui 
import pandas as pd
import os
import requests
from time import sleep

def getLoginData():
   """
   @returns: login data
   """

   script_dir = os.path.dirname(__file__)
   data_dir   = os.path.join(script_dir, 'data') 
   login_path = os.path.join(data_dir, 'login.xlsx')

   login_data = pd.read_excel(login_path)
   return login_data

def login(user, pwd):
   pyautogui.PAUSE = 1.2

   # open navigator
   pyautogui.press('win')
   pyautogui.write('chrome')
   pyautogui.press('enter')

   # set full screen an open new tab
   pyautogui.hotkey('fn', 'f11')
   pyautogui.click(x=417, y=454)
   pyautogui.hotkey('ctrl', 't')

   # connect with website
   url = 'http://localhost:4200'
   if(testWebConn(url)): 
      pyautogui.write(url)

      pyautogui.PAUSE = 5

      pyautogui.press('enter')
   else:
      return
  
   # login
   pyautogui.click(x=1057, y=355, clicks=2)
   pyautogui.PAUSE = 1
   pyautogui.write(str(user))
   pyautogui.press('tab')
   pyautogui.write(str(pwd))
   pyautogui.click(x=1011, y=476)

def getPosition():
   sleep(10)
   print(pyautogui.position())

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

loginData = getLoginData()
user = loginData['LOGIN'][0]
pwd  = loginData['SENHA'][0]

login(user, pwd)
#getPosition()