import telebot
from dotenv import load_dotenv
import os
from download_comics import get_comic


def main():
    load_dotenv()
    comic_channel_id = os.environ['CHAT_ID']
    bot_token = os.environ['BOT_TOKEN']
    filename = 'comic.png'
    get_comic(filename)
    bot = telebot.TeleBot(bot_token)
    bot.send_photo(comic_channel_id, photo=open(filename, 'rb'), caption='Новая смеяка для вашей ржаки')
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
