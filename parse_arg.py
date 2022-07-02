import argparse

def parse_arguments(description):
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        "--image-dir",
        help="A path to images folder",
        default="./images",
    )
    return parser.parse_args()
