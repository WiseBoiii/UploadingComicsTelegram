import requests


def download_comic_image(comic_image_link, filename):

    response = requests.get(comic_image_link)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)


def get_comic(filename):
    url = 'https://xkcd.com/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    about_comic_json = response.json()
    comic_image_link = about_comic_json['img']
    download_comic_image(comic_image_link, filename)




