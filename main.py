from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = "7229502745:AAFzt5agcRUU8LVlzNZUk83lkIlJVJbmtR8"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Working on v1 code")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()