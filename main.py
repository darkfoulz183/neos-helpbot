import os
from flask import Flask, request
import telebot

API_TOKEN = os.environ.get('7111927585:AAHYNuD2Q_H4dpIIu3rF4XqGn-Hfk6OazLs')
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    update = request.get_json()
    if 'message' in update:
        msg = update['message']
        chat_id = msg['chat']['id']
        text = msg.get('text', '')
        if text == '/help':
            bot.send_message(chat_id, "🆘 Поддержка: support@valeria-lukyanova.com")
        elif text == '/policy':
            bot.send_message(chat_id, "📜 Политика конфиденциальности:\nhttps://www.valeria-lukyanova.com/term")
    return 'OK'
