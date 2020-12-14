import pyautogui
import keyboard
import time
import random
from alive_progress import alive_bar


def countdown(sec):
    while not (sec < 0):
        timer = sec
        print("Spaming in ", timer, end="\r")
        time.sleep(1)
        sec -= 1


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
interval = float(input("Time interval(sec) : "))

# input time in seconds
sec = 5

# function call
countdown(int(sec))

with alive_bar(count, title="Spaming!", spinner="classic") as bar:
    for _ in range(count):
        pyautogui.typewrite(random.choice(spamText))
        pyautogui.press('enter')
        time.sleep(interval)
        bar()
print('\nDone')

print("Press any key to continue")
keyboard.read_key()
print("Happy hacking...! ;-)")
