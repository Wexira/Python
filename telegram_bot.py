

import bot

bot = Bot('1001825359:AAHBZpu6byz6BzJGXn1uzOk2DXukMo0vLLw')

@bot.message_handler(content_types=['text'])
def send_echo(message):
    # bot.reply_to(message, message.text)
    bot.send_message(message.chat.id, message.text)

    bot.polling( none_stop = True )
