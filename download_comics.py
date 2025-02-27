import requests
import os


def download_comic_image(comic_image_link, filename):

    response = requests.get(comic_image_link)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)


def get_comic(filename):
    url = 'https://xkcd.com/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    all_about_comic = response.json()
    comic_image_link = all_about_comic['img']
    download_comic_image(comic_image_link, filename)




