import requests
import os


url = 'https://xkcd.com/info.0.json'


def download_comic_image(comic_image_link):
    filename = 'comic'
    comic_image = requests.get(comic_image_link)
    comic_image.raise_for_status()
    with open(f'{filename}.png', 'wb') as file:
        file.write(comic_image.content)


response = requests.get(url)
response.raise_for_status()
all_about_comic = response.json()
comic_image_link = all_about_comic['img']
funny_comment = all_about_comic['alt']
download_comic_image(comic_image_link)


