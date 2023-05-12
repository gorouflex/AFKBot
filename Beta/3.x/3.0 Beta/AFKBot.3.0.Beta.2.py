# Version 2.9.1 (2A921R) Portable
import os
import secrets
import sys
import webbrowser
import customtkinter as ctk
import pyautogui
from PIL import Image

ctk.set_default_color_theme("dark-blue")
ctk.set_appearance_mode("dark")

def open_github():
    webbrowser.open("https://www.github.com/gorouflex/afkbot")


def resource_path(relative_path):
    base_path = getattr(sys, '_MEI PASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


class Main(ctk.CTk):
    KEYS = ['a', 's', 'd', 'w', ' ']
    SLEEP_TIME = 3

    def __init__(self):
        super().__init__()
        self.is_running = None
        self.window = self
        self.geometry("215x315")
        self.resizable(False, False)
        self.update_title()
        self.columnconfigure(0, weight=1)
        icon_path = os.path.join(os.getcwd(), "assets", "app.ico")
        self.iconbitmap(icon_path)
        img_path = os.path.join(os.getcwd(), "assets", "bg.png")
        self.bg_img = ctk.CTkImage(Image.open(img_path), size=(800, 400))
        self.bg_label = ctk.CTkLabel(self, text="", image=self.bg_img)
        self.bg_label.place(relx=0.5, rely=0.5, anchor="center")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, columnspan=2, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="AFKBot by GorouFlex", font=ctk.CTkFont(size=18, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 5))
        self.start_button = ctk.CTkButton(self.sidebar_frame, width=80, height=50, text="Start", font=("", 16, "bold"),
                                          corner_radius=10,
                                          command=self.start)
        self.start_button.grid(row=1, column=0, padx=20, pady=(20, 10))
        self.stop_button = ctk.CTkButton(self.sidebar_frame, width=80, height=50, text="Stop", font=("", 16, "bold"),
                                         corner_radius=10,
                                         command=self.stop)
        self.stop_button.grid(row=2, column=0, padx=20, pady=10)
        self.github_button = ctk.CTkButton(self.sidebar_frame, width=80, height=50, text="Info",
                                           font=("", 16, "bold"),
                                           corner_radius=10,
                                           command=open_github)
        self.github_button.grid(row=3, column=0, padx=20, pady=10)
        self.credit_label = ctk.CTkLabel(self, width=1100,
                                         text="Ver 3.0 Beta 2", font=("", 16, "bold"))
        self.credit_label.grid(row=6, column=0, sticky="s")
        self.bind("<Escape>", self.stop)
    

    def update_title(self):
        self.title(secrets.token_hex(14))
        self.after(1000, self.update_title)

    def start(self):
        self.is_running = True
        self.press_keys()

    def stop(self):
        self.is_running = False

    def press_keys(self):
        options = {
            "keys": ['a', 's', 'd', 'w', ' '],
            "buttons": ['left', 'right'],
            "screen_size": (1920, 1080),
            "sleep_time": self.SLEEP_TIME * 1000
        }

        def get_random_option(options_list):
            return secrets.choice(options_list)

        def press_key(actions):
            pyautogui.press(actions)

        def click_button(click):
            pyautogui.click(button=click)

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
