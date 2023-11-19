import sys
import webbrowser
import customtkinter
import urllib3
import random
import threading
from assets.config import KeyPresser
import tkinter as tk
from tkinter import messagebox

def get_latest_version():
    latest_version = urllib3.request(url="https://github.com/gorouflex/afkbot/releases/latest", method="GET")
    latest_version = latest_version.geturl()
    return latest_version.split("/")[-1]

def open_github():
    webbrowser.open("https://www.github.com/gorouflex/afkbot")

def open_releases():
    webbrowser.open(f"https://github.com/gorouflex/afkbot/releases/tag/{get_latest_version()}")

def info_window():
    InfoWindow().mainloop()

def check_for_updates():
    local_version = "4.2.0"
    latest_version = get_latest_version()

    if local_version < latest_version:
        result = messagebox.askquestion(
            "Update Available",
            "A new update has been found! Please use the Updater to install the latest version.\nOtherwise, the app will exit.\nDo you want to visit the GitHub page for more details?",
            icon="warning"
        )
        if result == "yes":
            webbrowser.open("https://github.com/gorouflex/afkbot/releases/latest")
        sys.exit()
    elif local_version > latest_version:
        result = messagebox.askquestion(
            "AFKBot Beta Program",
            "Welcome to AFKBot Beta Program.\nThis build may not be as stable as expected.\nOnly for testing purposes!",
            icon="warning"
        )
        if result == "no":
            sys.exit()
        else:
            pass
    else:
        pass

key_presser = KeyPresser()

def start():
    key_presser.is_running = True
    thread = threading.Thread(target=key_presser.press_keys)
    thread.start()


def stop():
    key_presser.is_running = False

class InfoWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('About')
        self.geometry("250x250")
        self.resizable(False, False)
        
        self.logo_label = customtkinter.CTkLabel(self, text="About AFKBot", font=("", 19, "bold"))
        self.logo_label.pack(pady=5)

        self.owner_label = customtkinter.CTkLabel(self, text="Main developer: GorouFlex", font=("", 15))
        self.owner_label.pack(pady=2)

        self.subdev_label = customtkinter.CTkLabel(self, text="Sub-developer: NotchApple1703", font=("", 15))
        self.subdev_label.pack(pady=2)

        self.buttons = [
            ["Open Github", open_github],
            ["Change log", open_releases],
        ]

        for i in range(2):
            button = customtkinter.CTkButton(self, width=120, height=40, text=self.buttons[i][0], font=("", 16),
                                             corner_radius=5, command=self.buttons[i][1])
            button.pack(pady=5)

        self.version_label = customtkinter.CTkLabel(self, width=200,
                                                    text=f"Latest version on Github: {get_latest_version()}",
                                                    font=("", 14))
        self.version_label.pack(pady=5)

class MainWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('AFKBot')
        self.geometry("250x250")
        self.resizable(False, False)
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.logo_label = customtkinter.CTkLabel(self, text="AFKBot", font=("", 21, "bold"))
        self.logo_label.pack(pady=10)

        self.buttons = [
            ["Start", start],
            ["Stop", stop],
            ["About", info_window],
        ]
        
        for i in range(3):
            button = customtkinter.CTkButton(self, width=160, height=40, text=self.buttons[i][0], font=("", 16),
                                             corner_radius=5, command=self.buttons[i][1])
            button.pack(pady=5)

        self.version_label = customtkinter.CTkLabel(self, width=215, text=f"Version 4.2.0 (Stable)", font=("", 14))
        self.version_label.pack(pady=5)


def run_cli_mode():
    print("Welcome to AFKBot CLI Mode")
    print("Still in early stages!")

if __name__ == '__main__':
    if "--cli" in sys.argv:
        run_cli_mode()
    else:
        check_for_updates()
        app = MainWindow()
        app.mainloop()
