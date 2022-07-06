import argparse
import os
from urllib.parse import unquote, urlsplit

import requests


def save_image_from_url(url, save_path, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    ext = split_url_file_ext(url)
    image_path = f"{save_path}/{ext}"
    with open(image_path, "wb") as image:
        image.write(response.content)


def save_images(image_urls, save_path, filename, params=None):
    saved_images = []
    for index, image_url in enumerate(image_urls):
        ext = split_url_file_ext(image_url)
        image_path = f"{save_path}/{filename}_{index:03d}{ext}"
        save_image_from_url(image_url, image_path, params)
        saved_images.append(image_path)
    return saved_images


def split_url_file_ext(url):
    path = unquote(urlsplit(url).path)
    return os.path.splitext(path)[-1]
