from datetime import datetime
from pathlib import Path
from environs import Env
from urllib.parse import unquote, urlsplit
import argparse
import requests


from image_download import save_images


def fetch_random_nasa_apod_image_urls(api_key):
    image_urls = []
    counts_of_apod = 10
    response = requests.get(
        "https://api.nasa.gov/planetary/apod",
        params={"api_key": api_key, "count": counts_of_apod},
    )
    response.raise_for_status()
    for apod in response.json():
        if apod["media_type"] == "image":
            image_urls.append(apod["url"])
    return image_urls


def fetch_nasa_epic_image_urls(api_key):
    image_urls = []
    response = requests.get(
        "https://api.nasa.gov/EPIC/api/natural/images",
        params={"api_key": api_key},
    )
    response.raise_for_status()
    for image_metadata in response.json():
        image_name = image_metadata["image"]
        image_datetime = datetime.fromisoformat(image_metadata["date"])
        image_date = image_datetime.strftime("%Y/%m/%d")
        image_urls.append(
            f"https://api.nasa.gov/EPIC/archive/natural/{image_date}"
            f"/png/{image_name}.png"
        )
    return image_urls


if __name__ == "__main__":
    args = "The script allows you to download images from NASA API."
    parser = argparse.ArgumentParser(description=args)
    parser.add_argument(
        "--image-dir",
        help="A path to images folder",
        default="./images",
    )
    image_dir = parser.image_dir
    Path(image_dir).mkdir(parents=True, exist_ok=True)
    spacex_image_urls = fetch_spacex_latest_launch_image_urls()
    env = Env()
    env.read_env()
    nasa_api_key = env.str("NASA_API_KEY")
    Path(image_dir).mkdir(parents=True, exist_ok=True)
    nasa_apod_image_urls = fetch_random_nasa_apod_image_urls(nasa_api_key)
    nasa_epic_image_urls = fetch_nasa_epic_image_urls(nasa_api_key)

    save_images(nasa_apod_image_urls, image_dir, "nasa_apod")
    save_images(
        nasa_epic_image_urls, image_dir, "nasa_epic", {"api_key": nasa_api_key}
    )
