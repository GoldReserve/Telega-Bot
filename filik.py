from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
# from conv import *
from conf_ig import conf

bot = Bot(token=conf())
updater = Updater(token=conf(), use_context=True)
dispatcher = updater.dispatcher
GENDER, PHOTO, LOCATION, BIO = range(4)


def start(update, context):
    arg = context.args
    if not arg:
        context.bot.send_message(update.effective_chat.id, "Привет")
    else:
        context.bot.send_message(update.effective_chat.id, f"{' '.join(arg)}")


def info(update, context):
    context.bot.send_message(update.effective_chat.id, "Меня создала компания GB!")


def message(update, context):
    text = update.message.text
    if text.lower() == 'привет':
        context.bot.send_message(update.effective_chat.id, 'И тебе привет..')
    else:
        context.bot.send_message(update.effective_chat.id, 'я тебя не понимаю')


def unknown(update, context):
    context.bot.send_message(update.effective_chat.id, f'Шо сказал, не пойму')


start_handler = CommandHandler('start', start)
info_handler = CommandHandler('info', info)

# conv_handler = ConversationHandler( # здесь строится логика разговора
#         # точка входа в разговор
#         entry_points=[CommandHandler('start', start)],
#         # этапы разговора, каждый со своим списком обработчиков сообщений
#         states={
#             GENDER: [MessageHandler(Filters.regex('^(Boy|Girl|Other)$'), gender)],
#             PHOTO: [MessageHandler(Filters.photo, photo), CommandHandler('skip', skip_photo)],
#             LOCATION: [
#                 MessageHandler(Filters.location, location),
#                 CommandHandler('skip', skip_location),
#             ],
#             BIO: [MessageHandler(Filters.text & ~Filters.command, bio)],
#         },
#         # точка выхода из разговора
#         fallbacks=[CommandHandler('cancel', cancel)],
#     )
message_handler = MessageHandler(Filters.text, message)
#unknown_handler = MessageHandler(Filters.command, unknown) #/game

#dispatcher.add_handler(conv_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(info_handler)
#dispatcher.add_handler(unknown_handler)
dispatcher.add_handler(message_handler)

print('server started')
updater.start_polling()
updater.idle()