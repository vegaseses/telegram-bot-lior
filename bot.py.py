from telegram.ext import Updater, CommandHandler

TOKEN = '7659087531:AAEgrHADdHUk2eu73RxMuA_KS45pkIz8q0Q'

def start(update, context):
    update.message.reply_text("Welcome to Lior Robot")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()