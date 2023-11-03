import os
import urllib3
import zipfile
import customtkinter as ctk

LATEST_RELEASE_URL = "https://github.com/gorouflex/afkbot/releases/latest"
DOWNLOAD_URL = "https://github.com/gorouflex/afkbot/releases/latest/download/AFKBot.zip"

def get_latest_version():
    http = urllib3.PoolManager()
    response = http.request('GET', LATEST_RELEASE_URL)
    latest_version = response.geturl().split("/")[-1]
    return latest_version

def download_and_extract(url, filename):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    with open(filename, "wb") as f:
        f.write(response.data)
    with zipfile.ZipFile(filename, "r") as zip_ref:
        zip_ref.extractall()
    os.remove(filename)

def update_afkbot():
    download_and_extract(DOWNLOAD_URL, "AFKBot.zip")
    caution_label.configure(text="Update successfully!")

root = ctk.CTk()
root.geometry("450x100")
root.title("AFKBot Updater V4.0.1")

caution_label = ctk.CTkLabel(root, text="It might take 20s (depend on your internet) to download and update")
caution_label.pack(pady=5)

update_button = ctk.CTkButton(root, text="Update (AFKBot)", command=update_afkbot)
update_button.pack(pady=1)

version_label = ctk.CTkLabel(root, text=f"Latest version on GitHub: {get_latest_version()}")
version_label.pack(side="bottom")

root.mainloop()
