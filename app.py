import serial #Serial imported for Serial communication
import time #Required to use delay functions
import pyautogui
import IPython
open = False
ArduinoSerial = serial.Serial('COM5',9600) #Create Serial port object called arduinoSerial
time.sleep(2) #wait for 2 seconds for the communication to get established
while 1:
  incoming = str (ArduinoSerial.readline()) #read the serial data and print it as line
  print (incoming)
  if 'DESKTOP' in incoming and open == False:
    pyautogui.keyDown('winleft')
    pyautogui.press('d')
    pyautogui.keyUp('winleft')
    print ("HIDE")
    open = True
  elif 'DESKTOP' in incoming and open == True:
    break
    # pin = int(input("Please enter your PIN to reset: "))
    # if pin == 1234:
    #     open = False
    #     print ("RESET")
    #     pyautogui.keyDown('winleft')
    #     pyautogui.press('d')
    #     pyautogui.keyUp('winleft')
    #     open = True
    #     continue
    # else:
    #     print ("INCORRECT PIN")
    #     continue
    
    #donothing
#   if 'APP' in incoming:
#     # pyautogui.keyDown('winleft')
#     # pyautogui.press('d')
#     # pyautogui.keyUp('winleft')
#     print ("SHOW")
#     # pyautogui.hotkey('winkey', 'd') 