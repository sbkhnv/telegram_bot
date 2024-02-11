import os
import telebot
from dotenv import load_dotenv
data = load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    user=message.from_user
    bot.reply_to(message, f"{user.first_name} hi dude whats up?")

@bot.message_handler(commands=['About_me'])
def send_welcome(message):
    user=message.from_user
    bot.reply_to(message, f"{user.first_name} thank u for using me iam created by @subkhanov77 in 11-02-2023")

@bot.message_handler(commands=['channels'])
def send_welcome(message):
    user=message.from_user
    bot.reply_to(message, f"""dear {user.first_name}
    here is channels which is owned by @subkhanov77\n\n@bbb8onl\n@sbkhnv\n@fx_eminent
    """)


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, """
    tinchlimi?
@subkhanov77 yozas brat man javob yozomiman :)
    """)

if __name__ == "__main__":
    bot.infinity_polling()
