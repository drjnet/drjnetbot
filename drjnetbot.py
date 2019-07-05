#!/usr/bin/python

import os, requests, json, pprint, telebot, logging, traceback
import config

# Grab BTC Prices from blockchain.info
# r = requests.get("https://blockchain.info/ticker") 
# json_data = json.loads(r.text)
   
# Store prices in strings for output
# price_gbp = "GBP" + str((json_data['GBP']['last']))
# price_euro = "EUR" + str((json_data['EUR']['last']))
# price_output="Latest BTC Price \n------------------\n" + price_gbp + " / " + price_euro
# print (price_output)


def get_prices(currency):
    price = 0
    r = requests.get("https://blockchain.info/ticker") 
    json_data = json.loads(r.text)
    price=int(round((json_data[currency]['last'])))
    return price

priceTicker = "EUR " + str(get_prices("EUR")) + " / " + "GBP " + str(get_prices("GBP"))

print priceTicker

token = "{telegramtoken}"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome friend. Type /price for latest BTC price in euro and gbp")

@bot.message_handler(commands=['price'])
def send_welcome(message):
    bot.reply_to(message, priceTicker)

bot.polling()