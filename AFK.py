import pyautogui
import random
import threading
import webbrowser
from tkinter import *

def start():
    global stop_flag
    stop_flag = False
    t = threading.Thread(target=press_keys)
    t.start() 

def pause():
    global pause_flag
    pause_flag = not pause_flag

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

def open_github():
    webbrowser.open('https://github.com/gorouflex/afkbot')

root = Tk()
root.geometry("500x300")
root.resizable(0, 0)
root.title(''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=random.randint(10,24))))
bg_img = PhotoImage(file = "background.png")
bg_img = bg_img.subsample(2, 2)
bg = Label(root, image = bg_img, width=500, height=300)
bg.grid(row=0, column=0, rowspan=4, sticky='nsew')

start_button = Button(root, text="Start", command=start, font=("Helvetica", 12))
start_button.grid(row=0, column=0)

stop_button = Button(root, text="Stop", command=stop, font=("Helvetica", 12))
stop_button.grid(row=1, column=0)

pause_button = Button(root, text="Pause", command=pause, font=("Helvetica", 12))
pause_button.grid(row=2, column=0)

github_button = Button(root,text="Github",command=open_github ,font=("Helvetica", 12))
github_button.grid(row=3,column=0)

credit_label = Label(root,text="Credit: GorouFlex aka KRJ", font=("Helvetica", 12))
credit_label.grid(row=3,column=1)

def update_title():
    root.title(''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=random.randint(10,24))))
    root.after(1000, update_title)

update_title()
root.bind('<Escape>', lambda e: root.destroy())
root.mainloop()
