from pynput.keyboard import Key, Listener, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import time
import threading
import tkinter as tk

keyboard = KeyboardController()
mouse = MouseController()

def press_keys():
    for _ in range(3):
        keyboard.press('a')
        time.sleep(2)
        keyboard.release('a')
        keyboard.press('s')
        time.sleep(2)
        keyboard.release('s')
        keyboard.press('d')
        time.sleep(2)
        keyboard.release('d')
        keyboard.press('w')
        time.sleep(2)
        keyboard.release('w')

def click_mouse():
    for _ in range(5):
        mouse.click(Button.right)
    for _ in range(4):
        mouse.click(Button.left)

def loop():
    while run:
        press_keys()
        click_mouse()
        time.sleep(0.1)

def start():
    global run
    run = True
    t = threading.Thread(target=loop)
    t.start()

def stop():
    global run
    run = False

def on_press(key):
    if key == Key.esc:
        stop()

root = tk.Tk()
root.title("Spamming Script")

frame = tk.Frame(root)
frame.pack()

start_button = tk.Button(frame, text="Start", command=start)
start_button.pack(side=tk.LEFT)

stop_button = tk.Button(frame, text="Stop", command=stop)
stop_button.pack(side=tk.LEFT)

listener = Listener(on_press=on_press)
listener.start()

root.mainloop()