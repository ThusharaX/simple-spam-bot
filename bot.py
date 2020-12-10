import pyautogui
import keyboard
import time
import random


def countdown(s):
    while s:
        timer = s
        print("Spaming in ", timer, end="\r")
        time.sleep(1)
        s -= 1


spamText = []
count = 0

flag = 'y'

while (flag == 'y'):
    text = input("Spam Text : ")
    spamText.append(text)
    flag = input("Do you want to add more messages(y/n) : ")
    if (flag == 'n'):
        break

count = int(input("How many times : "))

# input time in seconds
s = 5

# function call
countdown(int(s))
print('\nSpaming!!')

for _ in range(count):
    pyautogui.typewrite(random.choice(spamText))
    pyautogui.press('enter')
    time.sleep(2)
print('Done')

print("Press any key to continue")
keyboard.read_key()
print("Happy hacking...! ;-)")
