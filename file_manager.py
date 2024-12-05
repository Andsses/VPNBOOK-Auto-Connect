import os

class FileManager:
    def __init__(self, download_folder):
        self.download_folder = download_folder
        # Ensure the folder exists
        os.makedirs(self.download_folder, exist_ok=True)
    
    def clear_folder(self):
        """Empty a folder by deleting all files."""
        if os.path.exists(self.download_folder):  # Ensure the folder exists
            for file in os.listdir(self.download_folder):
                file_path = os.path.join(self.download_folder, file)
                if os.path.isfile(file_path):
                    os.unlink(file_path)
        else:
            print(f"Error: The folder {self.download_folder} does not exist.")
