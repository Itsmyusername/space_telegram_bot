from pathlib import Path
import argparse
import requests

from image_download import save_images


def fetch_spacex_latest_launch_image_urls():
    response = requests.get("https://api.spacexdata.com/v4/launches/latest")
    response.raise_for_status()
    return response.json()["links"]["flickr"]["original"]


if __name__ == "__main__":
    args = "The script allows you to download images from NASA API."
    parser = argparse.ArgumentParser(description=args)
    parser.add_argument(
        "--image-dir",
        help="A path to images folder",
        default="./images",
    )
    image_dir = parser.image_dir

    save_images(spacex_image_urls, image_dir, "spacex")
