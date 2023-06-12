# Simple Updater V3 for AFKBot
import re
import sys
import zipfile
import customtkinter as ctk
import os
import requests

url = 'https://github.com/gorouflex/afkbot/releases/latest/download/AFKBot.zip'

ctk.set_appearance_mode("dark")

latest_version = None


def resource_path(relative_path):
    base_path = getattr(sys, '_MEI PASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def get_latest_version():
    global latest_version
    if latest_version is None:
        response = requests.get('https://github.com/gorouflex/afkbot/releases/latest')
        latest_version = re.search(r'releases/tag/(\d+\.\d+(\.\d+)?)', response.text).group(1)
    return latest_version


def download_file():
    r = requests.get(url)
    with open('AFKBot.zip', 'wb') as f:
        f.write(r.content)
    with zipfile.ZipFile('AFKBot.zip', 'r') as zip_ref:
        zip_ref.extractall()
    caution_label.configure(text="Update successfully!")
    os.remove("AFKBot.zip")


root = ctk.CTk()
root.geometry("400x90")
root.title("AFKBot Updater V3")
caution_label = ctk.CTkLabel(root,
                             text="It might take 20s (depend on your internet) to download and update")
caution_label.pack(pady=1)
button = ctk.CTkButton(root, text="Update", command=download_file)
button.pack(pady=1)


version_label = ctk.CTkLabel(root, text=f"Latest version on GitHub: {get_latest_version()}")
version_label.pack(side="bottom")

root.mainloop()
