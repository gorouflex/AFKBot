# Version 4.0
import sys
import webbrowser
import customtkinter
import urllib3
import random
import threading
from assets.config import KeyPresser

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
            ["Changelog", open_releases],
        ]

        for i in range(2):
            button = customtkinter.CTkButton(self, width=120, height=40, text=self.buttons[i][0], font=("", 16),
                                             corner_radius=5, command=self.buttons[i][1])
            button.pack(pady=5)

        self.version_label = customtkinter.CTkLabel(self, width=200,
                                                    text=f"Latest version on github: {get_latest_version()}",
                                                    font=("", 14))
        self.version_label.pack(pady=5)


# Main app
class MainWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('AFKBot')
        self.title = "AFKBot"
        self.geometry("250x230")
        self.resizable(False, False)
        
        self.key_presser = KeyPresser()
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.logo_label = customtkinter.CTkLabel(self, text="AFKBot", font=("", 21, "bold"))
        self.logo_label.pack(pady=10)

        self.buttons = [
            ["Start", self.start],
            ["Stop", self.stop],
            ["About", info_window],
        ]
        
        for i in range(3):
            button = customtkinter.CTkButton(self, width=150, height=40, text=self.buttons[i][0], font=("", 16),
                                             corner_radius=5, command=self.buttons[i][1])
            button.pack(pady=5)

        self.version_label = customtkinter.CTkLabel(self, width=215, text=f"Version 4.0.0", font=("", 14))
        self.version_label.pack(pady=5)

    def start(self):
        self.key_presser.is_running = True
        thread = threading.Thread(target=self.key_presser.press_keys)
        thread.start()

    def stop(self):
        self.key_presser.is_running = False

if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
