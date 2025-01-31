import cloudscraper
import os
import requests, time

scraper = cloudscraper.create_scraper()  # Bypasses Cloudflare
image_url = "https://img.craiyon.com/"
url = "https://api.craiyon.com/v4"
class ImageManupulation:
    def __init__(self):
        self.folder = "images"
        self.image_url = "https://img.craiyon.com/"
        self.image_path = ''
    def save_image(self,prompt):
        """This function will retun the image path that is saved in the local directory"""
        payload = {
            "prompt": prompt,
            "token": None,
            "model": "auto",
            "negative_prompt": "",
            "size": "256x256"
        }

        response = scraper.post(url, json=payload)
        if response.status_code == 200:
            image_name = response.json()['images'][0]
            image_url=self.image_url + image_name
            print("GENERATED: ", image_url)
        else:
            print("Error:", response.status_code, response.text)
            return
        os.makedirs(self.folder, exist_ok=True)
    
        response = requests.get(image_url, stream=True)
            
        if response.status_code == 200:
            
            image_name = os.path.basename(image_url)
            image_path = os.path.join(self.folder, image_name)
            with open(image_path, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            self.image_path = image_path
            return os.path.abspath(image_path)
        else:
            print("Failed to download image")
                
    def delete_img(self):
        """Deletes the saved image if it exists."""
        if hasattr(self, "image_path") and os.path.exists(self.image_path):
            os.remove(self.image_path)
            print(f"Deleted: {self.image_path}")
        else:
            print("Image not found or path not set.")
        
        
# obj  = ImageManupulation()
# obj.save_image("Image of toy")
# time.sleep(5)
# obj.delete_img()
