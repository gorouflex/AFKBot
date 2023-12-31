import os
import zipfile
import customtkinter as ctk
from bs4 import BeautifulSoup
import urllib3
from urllib3.util import Retry

http = urllib3.PoolManager(retries=Retry(connect=5, read=2, redirect=5))

LATEST_RELEASE_URL = "https://github.com/gorouflex/afkbot/releases/latest"
DOWNLOAD_URL = "https://github.com/gorouflex/afkbot/releases/latest/download/AFKBot.zip"
BETA_RELEASE_URL = "https://github.com/gorouflex/afkbot/releases"

def get_latest_version():
    response = http.request('GET', LATEST_RELEASE_URL)
    return response.geturl().split("/")[-1]

def get_latest_beta_version():
    response = http.request('GET', BETA_RELEASE_URL)
    soup = BeautifulSoup(response.data, 'html.parser')
    beta_tags = soup.find_all('a', class_='Link--primary', href=lambda x: x and '/tag/' in x)
    if beta_tags:
        beta_versions = [tag.text.strip() for tag in beta_tags]
        beta_versions_with_beta = [ver for ver in beta_versions if 'Beta' in ver]
        if beta_versions_with_beta:
            return beta_versions_with_beta[0]
    return None

def download_and_extract(url, filename):
    response = http.request('GET', url)
    with open(filename, "wb") as f:
        f.write(response.data)
    with zipfile.ZipFile(filename, "r") as zip_ref:
        zip_ref.extractall()
    os.remove(filename)

def update_afkbot():
    download_and_extract(DOWNLOAD_URL, "AFKBot.zip")
    caution_label.configure(text="Stable update successfully!")

def update_beta_afkbot():
    beta_version = get_latest_beta_version()
    if beta_version:
        beta_version_url = beta_version.replace(" ", "-")
        beta_download_url = f"https://github.com/gorouflex/AFKBot/releases/download/{beta_version_url}/AFKBot-Beta.zip"
        print(f"Downloading from: {beta_download_url}")
        download_and_extract(beta_download_url, "AFKBot-Beta.zip")
        caution_label.configure(text="Beta update successfully!")
    else:
        caution_label.configure(text="No beta version found.")

root = ctk.CTk()
root.geometry("450x170")
root.title("AFKBot Updater V4.1")

caution_label = ctk.CTkLabel(root, text="It might take 20s (depending on your internet) to download and update")
caution_label.pack(pady=5)

update_button = ctk.CTkButton(root, text="Update (Stable)", command=update_afkbot)
update_button.pack(pady=1)

update_beta_button = ctk.CTkButton(root, text="Update (Beta)", command=update_beta_afkbot)
update_beta_button.pack(pady=1)

version_label = ctk.CTkLabel(root, text=f"Latest stable version on GitHub: {get_latest_version()}")
version_label.pack(side="top")

beta_version_label = ctk.CTkLabel(root, text=f"Latest beta version on GitHub: {get_latest_beta_version()}")
beta_version_label.pack(side="top")

root.mainloop()
