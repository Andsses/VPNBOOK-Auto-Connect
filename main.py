import os
import requests
from vpn_fetcher import VpnFetcher
from vpn_downloader import VpnDownloader
from credential_service import CredentialService
from file_manager import FileManager

# Configuration
URL = "https://www.vpnbook.com/freevpn"
URL_FACEBOOK = "https://www.facebook.com/VPNBookNews/"
DOWNLOAD_FOLDER = "vpn_downloads"
CREDENTIALS_FOLDER = "vpnbook_credentials"

# Initialization of classes
vpn_fetcher = VpnFetcher(URL)
vpn_downloader = VpnDownloader(DOWNLOAD_FOLDER)
file_manager = FileManager(DOWNLOAD_FOLDER)
credential_service = CredentialService(CREDENTIALS_FOLDER)

def main():
    print("Fetching VPN server options...")
    vpn_options = vpn_fetcher.fetch_vpn_options()
    
    if not vpn_options:
        print("No VPN options found.")
        return
    
    print("Available options:")
    for i, option in enumerate(vpn_options):
        print(f"{i + 1}. {option['name']}")
    
    choice = int(input("Select an option (number): ")) - 1
    if choice < 0 or choice >= len(vpn_options):
        print("Invalid selection.")
        return
    
    selected_option = vpn_options[choice]
    print(f"Selected: {selected_option['name']}")
    
    # Empty the download folder before starting
    print("Clearing the download folder...")
    file_manager.clear_folder()

    # Download and extract the file
    print("Downloading file...")
    zip_path = vpn_downloader.download_vpn(selected_option)
    print(f"File downloaded: {zip_path}")
    
    print("Extracting file...")
    vpn_downloader.extract_zip(zip_path)
    print(f"File extracted to {DOWNLOAD_FOLDER}")
    
    # Fetch credentials from the website (assuming the site contains the credentials)
    print("Fetching credentials...")
    credential_service.fetch_credentials_from_url(URL_FACEBOOK)
    
if __name__ == "__main__":
    main()
