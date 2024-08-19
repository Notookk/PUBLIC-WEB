import asyncio
import socketio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
WEB_URL = os.getenv('WEB_URL')
BACKEND_URL = os.getenv('BACKEND_URL')

sio = socketio.AsyncClient()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    join_button = InlineKeyboardButton("Join Mini App", url=WEB_URL)
    keyboard = [[join_button]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome to the Telegram Music Bot!", reply_markup=reply_markup)

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = ' '.join(context.args)
    if not query:
        await update.message.reply_text("Please provide a song name!")
        return

    await sio.emit('play_song', {'query': query})
    await update.message.reply_text(f"Searching and streaming {query}...")

async def main():
    print(f"Connecting to backend URL: {BACKEND_URL}")  # Debug statement to check the URL
    try:
        await sio.connect(BACKEND_URL, timeout=10)  # Adjust the timeout if needed
    except Exception as e:
        print(f"Error connecting to backend: {e}")
        return

    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("play", play))

    try:
        await application.run_polling()
    except Exception as e:
        print(f"Error running polling: {e}")

if __name__ == '__main__':
    asyncio.run(main())
