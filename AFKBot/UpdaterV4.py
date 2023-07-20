import os
import requests
import zipfile
import customtkinter as ctk

LATEST_RELEASE_URL = "https://github.com/gorouflex/afkbot/releases/latest"
DOWNLOAD_URL = "https://github.com/gorouflex/afkbot/releases/latest/download/AFKBot.zip"


def get_latest_version():
    response = requests.get(LATEST_RELEASE_URL)
    latest_version = response.url.split("/")[-1]
    return latest_version


def download_and_extract(url, filename):
    response = requests.get(url)
    with open(filename, "wb") as f:
        f.write(response.content)
    with zipfile.ZipFile(filename, "r") as zip_ref:
        zip_ref.extractall()
    os.remove(filename)


def update_afkbot():
    download_and_extract(DOWNLOAD_URL, "AFKBot.zip")
    caution_label.configure(text="Update successfully!")


root = ctk.CTk()
root.geometry("450x100")
root.title("AFKBot Updater V4")

caution_label = ctk.CTkLabel(root, text="It might take 20s (depend on your internet) to download and update")
caution_label.pack(pady=5)

update_button = ctk.CTkButton(root, text="Update (AFKBot)", command=update_afkbot)
update_button.pack(pady=1)

version_label = ctk.CTkLabel(root, text=f"Latest version on GitHub: {get_latest_version()}")
version_label.pack(side="bottom")

root.mainloop()
