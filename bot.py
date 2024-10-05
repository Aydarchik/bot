

from random import choice
import telebot
from config import token


bot = telebot.TeleBot(token)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])

@bot.message_handler(commands=['info'])
def handle_start(message):
    bot.send_message(message.chat.id, """\
Hi there, I am EchoBot.
I am here to prank your friends with calling to them or spam messages\
""")
    
@bot.message_handler(commands=['joke'])
def jokes(message):
    joke = choice(["— Че морда такая набитая? — Да один качок штангу уронил… — Тебе на рожу??? — Да нет, себе на ногу… — Так в чем дело? — А я засмеялся…", " — Доктор, я ходить буду? — Ну, если только под себя. — Доктор, а плавать??? — Ну, если будете много ходить."])
    bot.reply_to(message, joke)
@bot.message_handler(content_types=['photo'])
def photo(message):   
     fileID = message.photo[-1].file_id   
     file_info = bot.get_file(fileID)
     downloaded_file = bot.download_file(file_info.file_path)
     with open("image.jpg", 'wb') as new_file:
         new_file.write(downloaded_file)

bot.infinity_polling()