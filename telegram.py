import telebot
from dotenv import load_dotenv
import os
import time


def main():
    load_dotenv()
    comic_channel_id = os.getenv('CHAT_ID')
    bot_token = os.getenv('BOT_TOKEN')
    filename = 'comic.png'
    bot = telebot.TeleBot(bot_token)
    bot.send_photo(comic_channel_id, photo=open('comic.png', 'rb'), caption='Новая смеяка для вашей ржаки')
    filename = 'comic.png'
    try:
        with open(filename, 'rb') as photo:
            bot.send_photo(comic_channel_id, photo=photo, caption='Новая смеяка для вашей ржаки')
    except Exception as e:
        print(f"Ошибка при отправке или удалении файла: {e}")
    finally:
        os.remove(filename)
        print(f"Файл {filename} успешно удален")


if __name__ == "__main__":
    main()
