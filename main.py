from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler


TOKEN = '5513940923:AAEEOoRDz_tACeXlUWJcQvO8l_A3cDzzhGU'
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

# функция обработки команды '/start'
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="Привет! Я бот. Поговори со мной.")

# функция обработки текстовых сообщений
def echo(update, context):
    text = 'ECHO: ' + update.message.text 
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text=text)    

# функция обработки команды '/caps'
def game(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="Игра!!!")


    # if context.args:
    #     text_caps = ' '.join(context.args).upper()
    #     context.bot.send_message(chat_id=update.effective_chat.id, 
    #                             text=text_caps)
    # else:
    #     context.bot.send_message(chat_id=update.effective_chat.id, 
    #                             text='No command argument')
    #     context.bot.send_message(chat_id=update.effective_chat.id, 
    #                             text='send: /caps argument')

# функция обработки встроенного запроса
def inline_caps(update, context):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Convert to UPPER TEXT',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)

# функция обработки не распознных команд
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="Не понимаю, о чём вы.")

# обработчик команды '/start'
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)    

# обработчик текстовых сообщений
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

# обработчик команды '/game'
caps_handler = CommandHandler('game', game)
dispatcher.add_handler(caps_handler)

# обработчик встроенных запросов 
inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)

# обработчик не распознных команд
unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

# запуск прослушивания сообщений
updater.start_polling()
# обработчик нажатия Ctrl+C
updater.idle()