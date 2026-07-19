import requests
import telebot
import os

TOKEN = os.getenv("TOKEN")
API_KEY = os.getenv("API_KEY")
ADMIN_ID = int(os.getenv("ADMIN_ID")) # int قوشۇلدى

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Salom Akam. Bot tayyor.")

@bot.message_handler(commands=['demo'])
def demo(message):
    prompt = "Restoran uchun 10 tilda zamonaviy DEMO yozib ber. Narxi $2000"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
    data = {"contents":[{"parts":[{"text": prompt}]}]}
    r = requests.post(url, json=data)

    try:
        text = r.json()['candidates'][0]['content']['parts'][0]['text']
        bot.send_message(message.chat.id, text)
    except:
        bot.send_message(message.chat.id, "Xatolik yuz berdi. Keyinni qayta tekshiring.")

@bot.message_handler(commands=['zip'])
def zip_file(message):
    bot.send_message(ADMIN_ID, "Akam zip soradi")
    bot.send_message(message.chat.id, "ZIP 1 soatda tayyor boladi")

bot.polling()
