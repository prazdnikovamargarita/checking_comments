import telebot
from telebot import types
import config
import requests

bot = telebot.TeleBot(config.token)

HIDE_MARKUP = telebot.types.ReplyKeyboardRemove()

markup_for_menu = types.ReplyKeyboardMarkup(one_time_keyboard=False,  resize_keyboard=True)
markup_for_menu.add('Facebook', 'Связаться с менеджером', 'На других сервисах')
markup_for_menu.add('Вчера','Сегодня','Все')



