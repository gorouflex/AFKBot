# Version 3.2 (Stallatron)
# Import modules
import os
import re
import secrets
import sys
import webbrowser
import customtkinter as ctk
import requests

from assets.config import press_keys

# Set Appearance
ctk.set_default_color_theme("dark-blue")
ctk.set_appearance_mode("dark")

latest_version = None


def get_latest_version():
    global latest_version
    if latest_version is None:
        response = requests.get('https://github.com/gorouflex/afkbot/releases/latest')
        latest_version = re.search(r'releases/tag/(\d+\.\d+)', response.text).group(1)
    return latest_version


def open_github():
    webbrowser.open("https://www.github.com/gorouflex/afkbot")


def open_releases():
    webbrowser.open("https://github.com/gorouflex/afkbot/releases/tag/3.2")


# This resource_path works only for compile to exe
def resource_path(relative_path):
    base_path = getattr(sys, '_MEI PASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


# Info TopLevelWindow
class InfoWindow(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.open_github = None
        self.geometry("240x220")
        self.label = ctk.CTkLabel(self, text="About AFKBot",
                                  font=ctk.CTkFont(size=18, weight="bold"))
        self.label.grid(padx=10, pady=10, sticky="nsew")
        self.resizable(False, False)
        icon_path = os.path.join(os.getcwd(), "assets", "app.ico")
        self.after(250, lambda: self.iconbitmap(icon_path))
        self.title('About AFKBot')
        self.owner = ctk.CTkLabel(self, text="Made by GorouFlex with ♥", font=("", 16))
        self.owner.grid(padx=10, pady=5, sticky="nsew")
        self.github_button = ctk.CTkButton(self, width=100, height=35, text="GitHub",
                                           font=("", 16),
                                           corner_radius=5,
                                           command=open_github)
        self.github_button.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        self.releases_button = ctk.CTkButton(self, width=100, height=35, text="Changes logs",
                                             font=("", 16),
                                             corner_radius=5,
                                             command=open_releases)
        self.releases_button.grid(row=3, column=0, padx=10, pady=2, sticky="nsew")
        self.version_label = ctk.CTkLabel(self, width=215,
                                          text=f"Latest version on GitHub: {get_latest_version()}",
                                          font=ctk.CTkFont(size=14))
        self.version_label.grid(row=4, column=0, padx=10, pady=5, sticky="nsew")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)


# Main app
class Main(ctk.CTk):

    def __init__(self):
        super().__init__()
        # Create main window
        self.toplevel_window = None
        self.openinfowindow = None
        self.is_running = None
        self.window = self
        self.geometry("215x225")
        self.resizable(False, False)
        self.update_title()
        # Create elements in GUI
        self.columnconfigure(0, weight=1)
        icon_path = os.path.join(os.getcwd(), "assets", "app.ico")
        self.iconbitmap(icon_path)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, columnspan=1, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="AFKBot by GorouFlex",
                                       font=ctk.CTkFont(size=18, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(10, 10))
        self.start_button = ctk.CTkButton(self.sidebar_frame, width=100, height=37, text="Start", font=("", 16),
                                          corner_radius=5,
                                          command=self.start)
        self.start_button.grid(row=1, column=0, padx=20, pady=5)
        self.stop_button = ctk.CTkButton(self.sidebar_frame, width=100, height=37, text="Stop", font=("", 16),
                                         corner_radius=5,
                                         command=self.stop)
        self.stop_button.grid(row=2, column=0, padx=20, pady=5)
        self.about_button = ctk.CTkButton(self.sidebar_frame, width=100, height=37, text="About",
                                          font=("", 16),
                                          corner_radius=5,
                                          command=self.infowindow)
        self.about_button.grid(row=3, column=0, padx=20, pady=5)
        self.credit_label = ctk.CTkLabel(self, width=215,
                                         text="Version 3.2 (Stallatron)", font=ctk.CTkFont(size=14))
        self.credit_label.grid(row=4, column=0, sticky="s")
        # Useless key to exit
        self.bind("<Escape>", self.stop)

    def update_title(self):
        self.title(secrets.token_hex(3))
        self.after(1000, self.update_title)

    def start(self):
        self.is_running = True
        press_keys(self)

    def stop(self):
        self.is_running = False

    # Check if info window toplevel is on
    def infowindow(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = InfoWindow()
        else:
            self.toplevel_window.focus()


if __name__ == '__main__':
    app = Main()
    app.mainloop()
