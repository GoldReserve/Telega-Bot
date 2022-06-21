
print(' ================================')
print('Крестики - нолики')
print(' Играем с ботом!')
print('')

pole = '*********'                                  # Поле - 9 ячеек, хотел списком, но мороки с проверкой много
step = 1                                            # Ходы - разделяем игроков по чет/нечет
sign = ''                                           # Символ X/O

def vision_pole(pole):                              # Функция отобрвжения поля
    for k in range(0,3):
        str_pole = ''
        for i in range(0,3):
            if pole[k*3+i] == '*': str_pole += str(k*3+i+1)
            if pole[k*3+i] != '*': str_pole += pole[k*3+i]
            if i < 2: str_pole += ' | '
        print(str_pole)
        print('----------')

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
while res != -1:
    if step%2 == 0: 
        sign = 'O'
        print('Ход бота')
        pole = iis(pole)
        vision_pole(pole)
        if len(check_win(pole,sign)) != 0:
            print(f'Победу одержали {sign} на {step} ходу ')
            print(f'Игра закончена!')
            break
        step += 1
    else: 
        sign = 'X'
        a = input(f'Ход {step} для {sign}, выберите поле: ')
        if a.isdigit():
            a = int(a)
            if a > 0 and a < 10:
                a -= 1
                if str(pole[a]) != '*': 
                    print('Эта ячейка уже занята !')
                    step -= 1
                else: pole = pole[:a] + sign + pole[a+1:]
            vision_pole(pole)
            if len(check_win(pole,sign)) != 0:
                print(f'Победу одержали {sign} на {step} ходу ')
                print(f'Игра закончена!')
                break
            step += 1
            if step == 10: 
                res = -1
                print(f'Игра закончена! Ничья! ')