import telebot
from dotenv import load_dotenv
import os


load_dotenv()
comic_channel_id = os.getenv('CHAT_ID')
bot_token = os.getenv('BOT_TOKEN')


def post_comic(chat_id):
    bot.send_photo(chat_id, photo=open('comic.png', 'rb'), caption='Новая смеяка для вашей ржаки')


bot = telebot.TeleBot(bot_token)
post_comic(comic_channel_id)
