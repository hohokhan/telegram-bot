from telegram import Bot
import datetime

# آیدی کانال‌ها + پیام‌ها
channels = {
    '-1002033033163': 'بغل میخوام، بغلم کن.',
    '-1002092678971': "Don't smoke, I love you."
}

# توکن ربات از سکرت گیت‌هاب
import os
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = Bot(token=TOKEN)

def send_messages():
    for chat_id, message in channels.items():
        try:
            bot.send_message(chat_id=chat_id, text=message)
            print(f"[{datetime.datetime.now()}] Sent to {chat_id}")
        except Exception as e:
            print(f"Failed to send to {chat_id}: {e}")

send_messages()
