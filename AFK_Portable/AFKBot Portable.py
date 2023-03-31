# Version 2.0 (2U76IB) Portable
import os
import sys
import secrets
import webbrowser
import random
import pyautogui
import customtkinter as ctk
from PIL import Image
ctk.set_appearance_mode("system_theme")
def open_github():
    webbrowser.open("https://www.github.com/gorouflex/afkbot")

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class Main(ctk.CTk):
    KEYS = ['a', 's', 'd', 'w', 'c', 'e', 'x', 'q']
    SLEEP_TIME = 3
    def __init__(self):
        super().__init__()
        self.window = self
        self.geometry("500x300")
        self.resizable(False, False)
        self.update_title()
        self.columnconfigure(0, weight=1)
        icon_path = os.path.join(os.getcwd(), "assets", "app.ico")
        self.iconbitmap(icon_path)        
        self.bg_img = ctk.CTkImage(Image.open("assets/bg.png"), size=(500, 300)) 
        self.bg_label = ctk.CTkLabel(self, text="", image=self.bg_img)
        self.bg_label.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.start_button = ctk.CTkButton(self, width=90, height=50, text="Start", font=("", 17, "bold"),
                                          corner_radius=10,
                                          background_corner_colors=("#ddd1dd", "#d4ceda", "#d4ceda", "#ddd1dd"),
                                          command=self.start)
        self.start_button.grid(row=0, column=0)
        self.stop_button = ctk.CTkButton(self, width=90, height=50, text="Stop", font=("", 17, "bold"),
                                         corner_radius=10,
                                         background_corner_colors=("#ddd1dd", "#d3c8d6", "#c8bdcd", "#f37c5e"),
                                         command=self.stop)
        self.stop_button.grid(row=1, column=0)
        self.github_button = ctk.CTkButton(self, width=90, height=50, text="GitHub", font=("", 17, "bold"),
                                           corner_radius=10,
                                           background_corner_colors=("#fc6f44", "#c2b1c3", "#ca8d94", "#e83515"),
                                           command=open_github)
        self.github_button.grid(row=2, column=0)
        self.credit_label = ctk.CTkLabel(self, width=500, text="Credit: GorouFlex | Portable Version 2.0 (2U76IB) | Codename: Sunset")
        self.credit_label.grid(row=3, column=0, sticky="s")
        self.bind("<Escape>", self.stop)
    def update_title(self):
        self.title(secrets.token_hex(14))
        self.after(1000, self.update_title)
    def start(self):
        self.is_running = True
        self.press_keys()
    def stop(self, event=None):
        self.is_running = False
        self.quit() 
    def press_keys(self):
        options = {
        "keys": ['a', 's', 'd', 'w', 'c', 'e', 'x', 'q'],
        "buttons": ['left', 'right'],
        "screen_size": (1920, 1080),
        "sleep_time": self.SLEEP_TIME * 1000
       }

        def get_random_option(options_list):
            return secrets.choice(options_list)
        def press_key(key):
            pyautogui.press(key)
        def click_button(button):
            pyautogui.click(button=button) 
        def move_mouse(x, y):
            pyautogui.moveTo(x, y)
        if not self.is_running:
            return
        key = get_random_option(options["keys"])
        button = get_random_option(options["buttons"])
        point = (secrets.randbelow(options["screen_size"][0]), secrets.randbelow(options["screen_size"][1]))
        press_key(key)
        click_button(button)
        move_mouse(*point)
        self.after(options["sleep_time"], self.press_keys)
if __name__ == '__main__':
    app = Main()
    app.mainloop()
