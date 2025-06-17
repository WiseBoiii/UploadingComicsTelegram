import requests
import random


def download_comic_image(image_url, filename):
    response = requests.get(image_url)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)


def get_comic(latest_comic_url, filename):
    response = requests.get(latest_comic_url)
    response.raise_for_status()
    latest_comic = response.json()
    max_number = latest_comic['num']

    random_number = random.randint(0, max_number)
    random_comic_url = f"https://xkcd.com/{random_number}/info.0.json"
    response = requests.get(random_comic_url)
    response.raise_for_status()
    comic = response.json()

    image_url = comic['img']
    download_comic_image(image_url, filename)

    return comic['alt']
