import os
import telebot
from dotenv import load_dotenv
from download_comics import get_comic


def main():
    load_dotenv()

    channel_id = os.environ['CHAT_ID']
    bot_token = os.environ['BOT_TOKEN']
    image_path = 'comic.png'
    latest_comic_url = 'https://xkcd.com/info.0.json'

    caption = get_comic(latest_comic_url, image_path)
    bot = telebot.TeleBot(bot_token)

    try:
        with open(image_path, 'rb') as image_file:
            bot.send_photo(chat_id=channel_id, photo=image_file, caption=caption)
    finally:
        os.remove(image_path)
        print(f"Файл {image_path} удалён")


if __name__ == "__main__":
    main()
