import os, requests, json, pprint
import telebot,unicodedata


# Grab BTC Prices from blockchain.info
r = requests.get("https://blockchain.info/ticker") 
json_data = json.loads(r.text)

def get_prices(currency):
    float price
    r = requests.get("https://blockchain.info/ticker") 
    json_data = json.loads(r.text)
    price=int(round((json_data[currency]['last'])))
    print price
    return price
    
print "Prices are " + price

# Store prices in strings for output
price_gbp=int(round((json_data['GBP']['last'])))
price_eur=int(round((json_data['EUR']['last'])))
print str(price_gbp) + str(price_eur)

price_gbp="GBP" + str((json_data['GBP']['last']))
price_euro="EUR" + str((json_data['EUR']['last']))
price_output="Latest BTC Price \n------------------\n" + price_gbp + " / " + price_euro
print price_output

# def show_prices ():
#     print "Latest BTC Price"
#     print "------------------"
#     print price_gbp + " / " + price_euro

# show_prices()

token = "860537932:AAGsD5o2ikSCoJzbmghlFovWBEy0MghOkE8"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome friend. Type /price for latest BTC price in euro and gbp")

@bot.message_handler(commands=['price'])
def send_welcome(message):
    bot.reply_to(message, price_output)

bot.polling()



