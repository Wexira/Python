# Добланутый бот

import pyowm
from py_telegram_bot.bot import Bot

owm = pyowm.OWM('49877e0901f8715065b4e76841918c56', language="ru")
bot = Bot('1001825359:AAHBZpu6byz6BzJGXn1uzOk2DXukMo0vLLw')
api = bot.get_api()

@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = owm.weather_at_place(place)
    w = observation.get_weather()
    temp = w.get_temperature('celsius')["temp"] 
    
    answer = "В городе " + place + " сейчас " + w.get_detailed_status() + "\n"
    answer += "Температура сейчас в районе " + str(temp) + "\n\n"

    if temp < 10:
        answer += "Сейчас ппц как холодно, одевайся как танк!"
    elif temp < 20:
        answer += "Сейчас холодно, оденься потеплее."
    else:
        answer += "Температура норм, одевай что угодно"

    bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True )



