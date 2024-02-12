import sys
import os
import webbrowser
import customtkinter
import urllib3
from bs4 import BeautifulSoup
import configparser
from configparser import ConfigParser
import secrets
import threading
import pyautogui
import time
import tkinter as tk
from tkinter import messagebox

is_running = False
info_window_instance = None
settings_window = None

http = urllib3.PoolManager()

def get_latest_version():
    latest_version = urllib3.request(url="https://github.com/gorouflex/afkbot/releases/latest", method="GET")
    latest_version = latest_version.geturl()
    return latest_version.split("/")[-1]

def get_latest_beta_version():
    response = http.request('GET', 'https://github.com/gorouflex/afkbot/releases')
    soup = BeautifulSoup(response.data, 'html.parser')
    if beta_tags := soup.find_all(
        'a', class_='Link--primary', href=lambda x: x and '/tag/' in x
    ):
        beta_versions = [tag.text.strip() for tag in beta_tags]
        if beta_versions_with_beta := [
            ver for ver in beta_versions if 'Beta' in ver
        ]:
            return beta_versions_with_beta[0]
    return None

    
def open_github():
    webbrowser.open("https://www.github.com/gorouflex/afkbot")

def open_releases():
    webbrowser.open(f"https://github.com/gorouflex/afkbot/releases/tag/{get_latest_version()}")

def info_window():
    global info_window_instance
    if info_window_instance is None or (hasattr(info_window_instance, 'winfo_exists') and not info_window_instance.winfo_exists()):
        info_window_instance = InfoWindow(app)
    else:
        info_window_instance.lift()

def check_for_updates():
    local_version = "4.3.1"
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

def start():
    global is_running
    if not is_running:
        is_running = True
        threading.Thread(target=press_keys).start()

def stop():
    global is_running
    is_running = False

def settings():
    global settings_window
    if settings_window is None or (hasattr(settings_window, 'winfo_exists') and not settings_window.winfo_exists()):
        settings_window = SettingsWindow(app)
    else:
        settings_window.lift()

class SettingsWindow(customtkinter.CTk):
    config_folder: str = 'Config'
    config_path: str = f'{config_folder}/config.txt'

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.title('Settings')
        self.geometry("520x290")
        self.resizable(False, False)

        self.logo_label = customtkinter.CTkLabel(self, text="Settings", font=("", 19, "bold"))
        self.logo_label.pack(pady=5)

        self.keys_label = customtkinter.CTkLabel(self, text="Keys:", font=("", 14, "bold"))
        self.keys_label.pack(pady=5)

        self.keys_entry = customtkinter.CTkEntry(
            self, placeholder_text="Keys", font=("", 15)
        )
        self.keys_entry.pack(pady=5)

        self.sleep_label = customtkinter.CTkLabel(self, text="Sleep time:", font=("", 14, "bold"))
        self.sleep_label.pack(pady=5)

        self.sleep_entry = customtkinter.CTkEntry(
            self, placeholder_text="Sleep time", font=("", 15)
        )
        self.sleep_entry.pack(pady=5)

        self.config_label = customtkinter.CTkLabel(
            self, width=215, text=f"Config folder: {os.getcwd()}/Config", font=("", 14)
        )
        self.config_label.pack(pady=5)

        self.save_button = customtkinter.CTkButton(self, text="Save", font=("", 15), command=self.create_config)
        self.save_button.pack(pady=5)

        self.load_config()

    def destroy(self):
        super().destroy()
        self.main_window.settings_window_closed()
        
    def create_config(self):
        sleep = self.sleep_entry.get()
        keys = self.keys_entry.get()

        if not sleep:
            sleep = '3'

        cfg: ConfigParser = ConfigParser()
        cfg.add_section('User')
        cfg.set('User', 'Sleep', sleep)
        cfg.set('User', 'keys', keys)

        with open(self.config_path, 'w', encoding='utf-8') as configfile:
            configfile.truncate(0)
            configfile.seek(0)
            cfg.write(configfile)

        self.config_label.configure(text=f"Config folder: {os.getcwd()}/Config")

    def load_config(self):
        cfg: ConfigParser = ConfigParser()
        if not os.path.exists(self.config_folder):
            os.mkdir(self.config_folder)
        if not os.path.isfile(self.config_path) or os.stat(self.config_path).st_size == 0:
            self.create_config()
            return
        cfg.read(self.config_path)
        if not cfg.has_section('User'):
            self.create_config()
            return

        try:
            keys = cfg.get('User', 'keys', fallback='ASWD ')
            sleep = cfg.get('User', 'Sleep', fallback='3')
            if not keys.strip():
               keys = 'ASWD '
            self.keys_entry.delete(0, 'end')
            self.keys_entry.insert(0, keys)
            self.sleep_entry.delete(0, 'end')
            self.sleep_entry.insert(0, sleep)
        except:
            self.create_config()

def press_keys():
    global is_running
    
    cfg: ConfigParser = ConfigParser()
    cfg.read(SettingsWindow.config_path)

    options = {
        "keys": cfg.get('User', 'keys', fallback='ASWD '),
        "buttons": ['left'],
        "sleep_time": cfg.getint('User', 'Sleep', fallback=3),
    }

    def get_random_option(options_list):
        return secrets.choice(options_list)

    def press_key(actions):
        pyautogui.press(actions)

    def click_button(click):
        pyautogui.click(button=click)

    while is_running:
        keys = options["keys"].strip() if options["keys"] else 'ASWD '
        key = get_random_option(keys)
        button = get_random_option(options["buttons"])
        press_key(key)
        click_button(button)
        time.sleep(options["sleep_time"])

class InfoWindow(customtkinter.CTk):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.title('About')
        self.geometry("290x290")
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
                                                    text=f"Latest stable version on Github: {get_latest_version()}",
                                                    font=("", 14))
        self.version_label.pack(pady=5)
        self.betaversion_label = customtkinter.CTkLabel(self, width=200,
                                                    text=f"Latest beta version on Github: {get_latest_beta_version()}",
                                                    font=("", 14))
        self.betaversion_label.pack(pady=2)

    def destroy(self):
        super().destroy()
        self.main_window.info_window_closed()
        
class MainWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('AFKBot')
        self.geometry("250x300")
        self.resizable(False, False)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.logo_label = customtkinter.CTkLabel(self, text="AFKBot", font=("", 21, "bold"))
        self.logo_label.pack(pady=10)

        self.buttons = [
            ["Start", start],
            ["Stop", stop],
            ["Settings", settings],
            ["About", info_window],
        ]

        for i in range(4):
            button = customtkinter.CTkButton(self, width=160, height=40, text=self.buttons[i][0], font=("", 16),
                                             corner_radius=5, command=self.buttons[i][1])
            button.pack(pady=5)

        self.version_label = customtkinter.CTkLabel(
            self, width=215, text="Version 4.3.1 Stable", font=("", 14)
        )
        self.version_label.pack(pady=5)

    def settings_window_closed(self):
        global settings_window
        settings_window = None

    def info_window_closed(self):
        global info_window_instance
        info_window_instance = None
        
if __name__ == '__main__':
    check_for_updates()
    app = MainWindow()
    app.mainloop()
