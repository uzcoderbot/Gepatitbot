
import json
import os
from telegram.ext import Updater, MessageHandler, Filters

# Load data
with open('data.json', 'r', encoding='utf-8') as f:
    qa_data = json.load(f)

def answer_question(update, context):
    if update.message.chat.type in ['group', 'supergroup']:
        question = update.message.text.lower()
        for item in qa_data:
            if item['question'].lower() in question:
                update.message.reply_text(item['answer'])
                return
        update.message.reply_text("Kechirasiz, bu savolga javob topilmadi.")

def main():
    token = os.getenv('BOT_TOKEN')
    if not token:
        print("Iltimos, BOT_TOKEN o'zgaruvchisini o'rnating.")
        return
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, answer_question))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
