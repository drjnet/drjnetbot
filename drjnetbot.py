# -*- coding: utf-8 -*-
#!/usr/bin/python

# TelegramBotAPI - Bhttps://pypi.org/project/pyTelegramBotAPI/

import os, requests, json, pprint, telebot, datetime
import config

# Grab latest BTC price data from blockchain.info and return price.
def get_prices(currency):
    price = 0
    r = requests.get("https://blockchain.info/ticker") 
    json_data = json.loads(r.text)
    price=int(round((json_data[currency]['last'])))
    return price

def get_help():
    f = open("welcome.md","r") 
    return f.read()

def get_datetime():
    currentDT = datetime.datetime.now()
    currentDT = currentDT.strftime("%Y-%m-%d %H:%M:%S")
    return currentDT

def write_log(message):
    currentDT = get_datetime()
    print str(currentDT) + " " + str(message)

## TelegramBot Stuff - ensure config.py exists and contains token!!
bot = telebot.TeleBot(config.telegramToken)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, get_help())
    write_log("Welcome message")
    
@bot.message_handler(commands=['price'])
def send_price(message):
    currentDT = get_datetime()
    priceTicker = "(DEV) Latest BTC price:\n" + str(currentDT) + "\nEUR " + str(get_prices("EUR")) + " / " + "GBP " + str(get_prices("GBP"))
    bot.reply_to(message, priceTicker)
    write_log("Prices requested")
    
bot.polling(none_stop=False, interval=0, timeout=20)