import csv
import requests
from io import BytesIO
import time
import random
import os

def download_images(csv_file, output_dir):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36"
    }

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(csv_file, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            image_url = row["IMAGE_URL"]
            image_filename = image_url.split('/')[-1]

            try:
                # Make a request to the image URL
                response = requests.get(image_url, headers=headers, stream=True)

                # Check the status code of the response
                if response.status_code == 200:
                    # Download the image in chunks to simulate browser behavior
                    with open(os.path.join(output_dir, image_filename), 'wb') as f:
                        for chunk in response.iter_content(chunk_size=1024):
                            if time.time() - start_time > 0.1:
                                time.sleep(0.1)
                                start_time = time.time()
                            f.write(chunk)

                    print(f"Image '{image_filename}' downloaded successfully.")
                else:
                    print(f"Failed to download image '{image_url}'. Status code: {response.status_code}")

            except requests.exceptions.RequestException as e:
                print(f"Failed to download image '{image_url}': {e}")

if __name__ == "__main__":
    csv_file = "images.csv"
    output_dir = "downloaded_images"

    download_images(csv_file, output_dir)
