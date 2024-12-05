import requests
from zipfile import ZipFile
import os

class VpnDownloader:
    def __init__(self, download_folder):
        self.download_folder = download_folder
    
    def download_vpn(self, option):
        """Downloads the ZIP file of the selected server."""
        response = requests.get(option['url'], stream=True)
        if response.status_code != 200:
            raise Exception("Error downloading the file.")
        
        zip_path = os.path.join(self.download_folder, os.path.basename(option['url']))
        with open(zip_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
        return zip_path
    
    def extract_zip(self, zip_path):
        """Extracts the downloaded ZIP file."""
        with ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(self.download_folder)
