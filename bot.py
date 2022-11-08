from telegram import Update
from telegram.ext import Updater, Filters, CommandHandler, MessageHandler, CallbackContext
from commands import *


updater = Updater('TOKEN HERE')

updater.dispatcher.add_handler(CommandHandler('start', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))
updater.dispatcher.add_handler(CommandHandler('sub', sub_command))
updater.dispatcher.add_handler(CommandHandler('mul', mul_command))
updater.dispatcher.add_handler(CommandHandler('div', div_command))
updater.dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), check_update))


updater.start_polling()
updater.idle()