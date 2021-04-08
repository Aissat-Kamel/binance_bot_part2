import configparser
import telepot
import time


config = configparser.ConfigParser()
config.read("config.ini")

bot_token = str(config["Telegram"]["bot_token"])

bot = telepot.Bot(bot_token)

def handle(msg):
    user_name = msg["from"]["first_name"] + " " + msg["from"]["last_name"]
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == "text":
        my_command = msg["text"]
        if "/start" in my_command:
            bot.sendMessage(chat_id, "Welcome "+user_name+" in your new bot!" )
        elif "/help" in my_command:
            bot.sendMessage(chat_id, "No help!" )

        else:
            bot.sendMessage(chat_id, "Uknow command" )


bot.message_loop(handle)

while True:
    time.sleep(20)
