import os
import telebot as tb
from telebot import types
import json as js
import string as str

bot = tb.TeleBot('6175663647:AAEbQ-yPVVz1UX33pINb-ktY3dkk1vmwoOM')


@bot.message_handler(commands=['developers'])
def developers(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Хухарев Денис', url='https://vk.com/huharev1'))
    markup.add(types.InlineKeyboardButton('Лазарев Семён', url='https://vk.com/lvzvrv'))
    markup.add(types.InlineKeyboardButton('Махонин Павел', url='https://vk.com/pmakhonin'))
    bot.reply_to(message, 'Список разработчиков', reply_markup=markup)


@bot.message_handler(commands=['parse'])
def parse(message):
    os.system("python SeleniumParser.py")
    bot.reply_to(message, 'Готово!')


@bot.message_handler(commands=['find', 'find'])
def find(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Поиск по символу', callback_data='symbol')
    btn2 = types.InlineKeyboardButton('Поиск по названию', callback_data='name')
    markup.row(btn1, btn2)
    bot.reply_to(message, 'Как будем искать?', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'symbol':
        bot.send_message(callback.from_user.id, "Введите название (Например: BTC)")
        bot.register_next_step_handler(callback.message, find_by_symbol)
    if callback.data == 'name':
        bot.send_message(callback.from_user.id, "Введите название (Например: Bitcoin)")
        bot.register_next_step_handler(callback.message, find_by_name)


@bot.message_handler(content_types=['text'])
def find_by_symbol(message):
    global symbol;
    symbol = message.text.upper()
    with open("ParseResult.json") as jsondata:
        data = js.load(jsondata)
    for i in data:
        if i['coin']['SYMBOL'] == symbol:
            names = "Название коина : " + i['coin']['NAME'] + "\n"
            names += "Символ коина : " + i['coin']['SYMBOL'] + "\n"
            names += "Цена коина : " + i['coin']['PRICE'] + "\n"
            names += "Рынок : " + i['coin']['MARKET_CAP'] + "\n"
            bot.send_message(message.from_user.id, names)


def find_by_name(message):
    global name;
    name = str.capwords(message.text)
    with open("ParseResult.json") as jsondata:
        data = js.load(jsondata)
    for i in data:
        if i['coin']['NAME'] == name:
            names = "Название коина : " + i['coin']['NAME'] + "\n"
            names += "Символ коина : " + i['coin']['SYMBOL'] + "\n"
            names += "Цена коина : " + i['coin']['PRICE'] + "\n"
            names += "Рынок : " + i['coin']['MARKET_CAP'] + "\n"
            bot.send_message(message.from_user.id, names)


bot.polling(none_stop=True)
