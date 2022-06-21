from telegram import InlineQueryResultArticle, InputTextMessageContent, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler

from conf_ig import conf


updater = Updater(token=conf())
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

def close_keyboard(update, context):
    update.message.reply_text('',reply_markup = ReplyKeyboardRemove())

# функция обработки команды '/game'
def game(update, context):
    reply_keyboard = [['/1','/2','/3'],['/4','/5','/6'],['/7','/8','/9']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    update.message.reply_text("Игра 'Крестики - нолики'", reply_markup=markup)

    pole = '*********'                                  # Поле - 9 ячеек, хотел списком, но мороки с проверкой много
    step = 1                                            # Ходы - разделяем игроков по чет/нечет
    sign = ''                                           # Символ X/O

    def vision_pole(pole):                              # Функция отобрвжения поля
        str_pole = ''
        for k in range(0,3):
            
            for i in range(0,3):
                if pole[k*3+i] == '*': str_pole += str(k*3+i+1)
                if pole[k*3+i] != '*': str_pole += pole[k*3+i]
                if i < 2: str_pole += ' | '
            str_pole += '\n'
        context.bot.send_message(chat_id=update.effective_chat.id, 
                             text=str_pole)

    def check_win(pole_st,st):
        win_comb = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]    #Выигрышные комбинации
        return [l for l in win_comb if pole_st[l[0]] == st and pole_st[l[1]] == st and pole_st[l[2]] == st]

    def iis(pol):
        import random
        new_pole = []
        new_pole = [l for l in range(0,len(pol)) if pol[l]=='*']
        f = lambda x,k: pol[:k] + x + pol[k+1:]
        for i in new_pole:
            pol = f('O',i)
            if len(check_win(pol,'O')) != 0: 
                return(pol)
            pol = f('*',i)
        for i in new_pole:    
            pol = f('X',i)
            if len(check_win(pol,'X')) != 0:
                pol = f('O',i)
                return(pol)
            pol = f('*',i)
        rand_shag = random.randrange(0, len(new_pole))
        pol = pol[:new_pole[rand_shag]] + 'O' + pol[new_pole[rand_shag]+1:]
        return(pol)



    vision_pole(pole)
    res = 0
    # while res != -1:
    #     if step%2 == 0: 
    #         sign = 'O'
    #         context.bot.send_message(chat_id=update.effective_chat.id, 
    #                          text='Мой ход...')
    #         pole = iis(pole)
    #         vision_pole(pole)
    #         if len(check_win(pole,sign)) != 0:
    #             txt = f'Победу одержали {sign} на {step} ходу \n Игра закончена!'
    #             context.bot.send_message(chat_id=update.effective_chat.id, 
    #                          text=txt)
    #             break
    #         step += 1

h1s_handler = CommandHandler('1', 1)
dispatcher.add_handler(h1s_handler)
    #    else: 
    #        sign = 'X'
    #        a = input(f'Ход {step} для {sign}, выберите поле: ')
    #         if a.isdigit():
    #             a = int(a)
    #             if a > 0 and a < 10:
    #                 a -= 1
    #                 if str(pole[a]) != '*': 
    #                     print('Эта ячейка уже занята !')
    #                     step -= 1
    #                 else: pole = pole[:a] + sign + pole[a+1:]
    #             vision_pole(pole)
    #             if len(check_win(pole,sign)) != 0:
    #                 print(f'Победу одержали {sign} на {step} ходу ')
    #                 print(f'Игра закончена!')
    #                 break
    #             step += 1
    #             if step == 10: 
    #                 res = -1
    #                 print(f'Игра закончена! Ничья! ')

# функция обработки не распознных команд
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="Не понимаю, о чём вы.")

# обработчик команды '/start'
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
start_handler = CommandHandler('stop', start)
dispatcher.add_handler(start_handler)      

# обработчик текстовых сообщений
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

# обработчик команды '/game'

game_handler = CommandHandler('game', game)
dispatcher.add_handler(game_handler)

# обработчик не распознных команд
unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

# запуск прослушивания сообщений
updater.start_polling()
# обработчик нажатия Ctrl+C
updater.idle()