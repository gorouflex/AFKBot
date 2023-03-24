import pyautogui
import random
import threading
from tkinter import *

def start():
    global stop_flag
    stop_flag = False
    t = threading.Thread(target=press_keys)
    t.start()
def stop():
    global stop_flag
    stop_flag = True
def press_keys():
    keys = ['a', 's', 'd', 'w', 'c', 'e', 'x', 'q']
    while not stop_flag:
        key = random.choice(keys)
        pyautogui.keyDown(key)
        pyautogui.sleep(2)
        pyautogui.keyUp(key)
        if random.random() < 0.5:
            pyautogui.click(button='right')
        else:
            pyautogui.click(button='left')
        x, y = random.randint(0, 1920), random.randint(0, 1080)
        pyautogui.moveTo(x, y)
root = Tk()
root.geometry("500x300")
root.title(''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=random.randint(10,24))))
start_button = Button(root, text="Start", command=start, font=("Helvetica", 16))
start_button.pack(pady=20)
stop_button = Button(root, text="Stop", command=stop, font=("Helvetica", 16))
stop_button.pack(pady=20)
credit_label = Label(root,text="Credit: GorouFlex aka KRJ", font=("Helvetica", 12))
credit_label.pack(side=BOTTOM,pady=10)
def update_title():
    root.title(''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=random.randint(10,24))))
    root.after(1000, update_title)
update_title()
root.bind('<Escape>', lambda e: root.destroy())
root.mainloop()