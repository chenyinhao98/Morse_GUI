from tkinter import *
import tkinter.font
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.OUT)

def dot():
    time.sleep(0.5)
    GPIO.output(10, True)
    time.sleep(0.5)
    GPIO.output(10, False)
    
    
def dash():
    time.sleep(0.5)
    GPIO.output(10, True)
    time.sleep(1.5)
    GPIO.output(10, False)
    
    
def charbreak():
    time.sleep(1.0)
    
def wordbreak():
    time.sleep(3.0)

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'}

MORSE_TO_GPIO_DICT= {'.': 'dot(), ', '-': 'dash(), ', ' ': 'charbreak(), '}

def encrypt(message): 
    cipher = '' 
    for letter in message: 
        if letter != ' ': 

            cipher += MORSE_CODE_DICT[letter] + ' '
        else: 
            cipher += ' '
  
    return cipher

def morseBlink(cipher):
    morse = ''
    for symbol in cipher:
        morse += MORSE_TO_GPIO_DICT[symbol]
    morse = morse.replace(' charbreak(), charbreak(),', ' wordbreak(),')          
    eval(morse)
    return morse
        
  
win = Tk()
win.title("MorseCodeBlink")
myFont = tkinter.font.Font(family = 'Helvetica', size = 15, weight = "bold")
                                  
def close(window):
    window.destroy()
    GPIO.cleanup()
    print("closewindow")

def convertAndBlink():
    global textInput
    userText = textInput.get()
    print(userText)
    textAsMorse = encrypt(userText.upper())
    print(textAsMorse)
    morseToBlink = morseBlink(textAsMorse)
    print(morseToBlink)
    


    

textInput = Entry(win, width=50)
textInput.pack()
textInput.focus_set()

sendButton = Button(win, text = 'OK', font = myFont, command = convertAndBlink, bg = 'white', height = 1, width = 24)
sendButton.pack(side= 'top')
closeButton = Button(win, text = 'QUIT', font = myFont, command = lambda: close(win), bg = 'white', height = 1, width = 24)
closeButton.pack(side = 'bottom')