# -*- coding: utf-8 -*-
#!/usr/bin/python

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

helpMessage = get_help()

## TelegramBot Stuff - ensure config.py exists and contains token!!
bot = telebot.TeleBot(config.telegramToken)
@bot.message_handler(commands=['start', 'help'])

def send_welcome(message):
    helpMessage = get_help()
    bot.reply_to(message, helpMessage)

@bot.message_handler(commands=['price'])
def send_price(message):
    currentDT = datetime.datetime.now()
    currentDT = currentDT.strftime("%Y-%m-%d %H:%M:%S")
    priceTicker = "(DEV) Latest BTC price:\n" + str(currentDT) + "\nEUR " + str(get_prices("EUR")) + " / " + "GBP " + str(get_prices("GBP"))
    bot.reply_to(message, priceTicker)
    print "Bot called at " + currentDT

bot.polling()