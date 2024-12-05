import requests
from bs4 import BeautifulSoup

class VpnFetcher:
    def __init__(self, url):
        self.url = url

    def fetch_vpn_options(self):
        """Fetches VPN server options from the website."""
        response = requests.get(self.url)
        if response.status_code != 200:
            raise Exception("Unable to access the VPNBook page.")
        
        soup = BeautifulSoup(response.text, 'html.parser')
        vpn_links = soup.select("ul.disc li a")
        vpn_options = [
            {"name": link.text.strip(), "url": f"https://www.vpnbook.com{link['href']}"}
            for link in vpn_links if link['href'].endswith('.zip')
        ]
        return vpn_options
