import pyautogui
import random
import threading
import webbrowser
import tkinter as tk
class AFKBot:
    def __init__(self, root):
        self.stop_flag = False
        self.pause_flag = False
        self.keys = ['a', 's', 'd', 'w', 'c', 'e', 'x', 'q']
        self.root = root
        self.root.geometry("500x300")
        self.root.resizable(False, False)
        self.root.title(''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=random.randint(10, 24))))
        self.bg_img = tk.PhotoImage(file="background.png").subsample(2, 2)
        self.bg = tk.Label(self.root, image=self.bg_img, width=500, height=300)
        self.bg.grid(row=0, column=0, rowspan=4, sticky='nsew')
        self.start_button = tk.Button(self.root, text="Start", command=self.start, font=("Helvetica", 12))
        self.start_button.grid(row=0, column=0, padx=0, pady=0)
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop, font=("Helvetica", 12))
        self.stop_button.grid(row=1, column=0, padx=0, pady=0)
        self.github_button = tk.Button(self.root, text="GitHub", command=self.open_github, font=("Helvetica", 12))
        self.github_button.grid(row=2, column=0, padx=0, pady=0)
        self.credit_label = tk.Label(self.root, text="Credit: GorouFlex aka KRJ | Version: 1.1 (1C46F)", font=("Helvetica", 12))
        self.credit_label.grid(row=3, column=0, padx=0, pady=0)
        self.root.bind('<Escape>', lambda e: self.root.destroy())
        self.update_title()
    def start(self):
        self.stop_flag = False
        threading.Thread(target=self.press_keys, daemon=True).start()
    def stop(self):
        self.stop_flag = True
    def press_keys(self):
        while not self.stop_flag:
            if not self.pause_flag:
                key = random.choice(self.keys)
                pyautogui.press(key)
                pyautogui.click(button=random.choice(['left', 'right']))
                pyautogui.moveTo(random.randint(0, 1920), random.randint(0, 1080))
                pyautogui.sleep(2)
    def open_github(self):
        webbrowser.open('https://github.com/gorouflex/afkbot')
    def update_title(self):
        self.root.title(''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=random.randint(10, 24))))
        self.root.after(1000, self.update_title)
if __name__ == '__main__':
    root = tk.Tk()
    bot = AFKBot(root)
    root.mainloop()
