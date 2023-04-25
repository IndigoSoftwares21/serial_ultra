import os
import sys
import serial #Serial imported for Serial communication
import time #Required to use delay functions
import pyautogui

def restart_program(ArduinoSerial):
    open = False
    time.sleep(2) #wait for 2 seconds for the communication to get established
    print("ARDUINO DETECTOR IS RUNNING.....")
    
    while True:
        incoming = str(ArduinoSerial.readline()) #read the serial data and print it as line
        print(incoming)
        if 'DESKTOP' in incoming and not open:
            pyautogui.keyDown('winleft')
            pyautogui.press('d')
            pyautogui.keyUp('winleft')
            print("HIDE")
            open = True
            pin = input("Enter pin: ")
            if pin == "1234":
                print("Restarting program...")
                ArduinoSerial.close()
                ArduinoSerial = serial.Serial('COM4',9600)
                restart_program(ArduinoSerial)
            else:
                print("Invalid code.")
                print("Closing...")
                time.sleep(2)
                ArduinoSerial.close()
                sys.exit()
        elif 'DESKTOP' in incoming and open:
            break

ArduinoSerial = serial.Serial('COM4',9600) #Create Serial port object called arduinoSerial
restart_program(ArduinoSerial)