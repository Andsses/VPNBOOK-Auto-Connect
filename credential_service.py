import requests
import re
import os

class CredentialService:
    def __init__(self, credentials_folder):
        self.credentials_folder = credentials_folder

    def extract_credentials(self, html_content):
        """Extracts the username and password from the web page using regular expressions."""
        match = re.search(r"Username: (\w+) Password: (\w+)", html_content)
        if match:
            username = match.group(1)
            password = match.group(2)
            return username, password
        return None, None

    def save_credentials(self, username, password):
        """Save credentials in .txt files."""
        os.makedirs(self.credentials_folder, exist_ok=True)
        with open(os.path.join(self.credentials_folder, 'username.txt'), 'w') as f:
            f.write(username)
        with open(os.path.join(self.credentials_folder, 'password.txt'), 'w') as f:
            f.write(password)

    def fetch_credentials_from_url(self, url):
        """Gets the HTML from the provided URL and extracts the credentials."""
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'es-ES,es;q=0.9',
            'cache-control': 'max-age=0',
            'dpr': '1.5',
            'priority': 'u=0, i',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera";v="114"',
            'sec-ch-ua-full-version-list': '"Chromium";v="128.0.6613.186", "Not;A=Brand";v="24.0.0.0", "Opera";v="114.0.5282.235"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.186 Safari/537.36',
            'viewport-width': '1226',
        }

        # Realizamos la solicitud HTTP
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            html_content = response.text
            username, password = self.extract_credentials(html_content)
            if username and password:
                self.save_credentials(username, password)
                print(f"Credentials saved: Username: {username} Password: {password}")
            else:
                print("No credentials found.")
        else:
            print(f"Error accessing the page. Status code: {response.status_code}")
