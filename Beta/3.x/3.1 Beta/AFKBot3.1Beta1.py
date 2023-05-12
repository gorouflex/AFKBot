# Version 3.1 Beta 1 (Stallatron)
import os
import secrets
import sys
import webbrowser
import customtkinter as ctk
import pyautogui

ctk.set_default_color_theme("dark-blue")
ctk.set_appearance_mode("dark")


def open_github():
    webbrowser.open("https://www.github.com/gorouflex/afkbot")

def open_releases():
    webbrowser.open("https://github.com/gorouflex/afkbot/releases")


def resource_path(relative_path):
    base_path = getattr(sys, '_MEI PASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


class InfoWindow(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.open_github = None
        self.geometry("250x175")
        self.label = ctk.CTkLabel(self, text="About AFKBot",
                                  font=ctk.CTkFont(size=18, weight="bold"))
        self.label.grid(padx=10, pady=10, sticky="nsew")
        icon_path = os.path.join(os.getcwd(), "assets", "app.ico")
        self.iconbitmap(icon_path)
        self.title('About')
        self.owner = ctk.CTkLabel(self, text="Made by GorouFlex with ♥", font=("", 16))
        self.owner.grid(padx=10, pady=5, sticky="nsew")
        self.github_button = ctk.CTkButton(self, width=20, height=35, text="GitHub",
                                           font=("", 16),
                                           corner_radius=10,
                                           command=open_github)
        self.github_button.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")
        self.releases_button = ctk.CTkButton(self, width=20, height=35, text="Releases",
                                           font=("", 16),
                                           corner_radius=10,
                                           command=open_releases)
        self.releases_button.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)


class Main(ctk.CTk):
    KEYS = ['a', 's', 'd', 'w', ' ']
    SLEEP_TIME = 3

    def __init__(self):
        super().__init__()
        self.toplevel_window = None
        self.openinfo = None
        self.is_running = None
        self.window = self
        self.geometry("215x225")
        self.resizable(False, False)
        self.update_title()
        self.columnconfigure(0, weight=1)
        icon_path = os.path.join(os.getcwd(), "assets", "app.ico")
        self.iconbitmap(icon_path)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, columnspan=2, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="AFKBot by GorouFlex",
                                       font=ctk.CTkFont(size=18, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.start_button = ctk.CTkButton(self.sidebar_frame, width=100, height=35, text="Start", font=("", 16),
                                          corner_radius=10,
                                          command=self.start)
        self.start_button.grid(row=1, column=0, padx=20, pady=5)
        self.stop_button = ctk.CTkButton(self.sidebar_frame, width=100, height=35, text="Stop", font=("", 16),
                                         corner_radius=10,
                                         command=self.stop)
        self.stop_button.grid(row=2, column=0, padx=20, pady=5)
        self.about_button = ctk.CTkButton(self.sidebar_frame, width=100, height=35, text="About",
                                         font=("", 16),
                                         corner_radius=10,
                                         command=self.infowindow)
        self.about_button.grid(row=3, column=0, padx=20, pady=5)
        self.credit_label = ctk.CTkLabel(self, width=215,
                                         text="Version 3.1 Beta 1", font=ctk.CTkFont(size=14))
        self.credit_label.grid(row=4, column=0, sticky="s")
        self.bind("<Escape>", self.stop)

    def update_title(self):
        self.title(secrets.token_hex(3))
        self.after(1000, self.update_title)

    def start(self):
        self.is_running = True
        self.press_keys()

    def stop(self):
        self.is_running = False

    def infowindow(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = InfoWindow()
        else:
            self.toplevel_window.focus()

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
