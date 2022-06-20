print(' ================================')
print('Консольный калькулятор')
print('')
operand = ['*','/','+','-', '(',')']
formula = (input(f'Введите выражение: ')).replace(' ','')

# Функция разбивает выражение на числа и операторы и закидывает все это в список
def dev_form(f_la,op_nd):
    tmp = ''
    list_f_la = []
    for i in range(0,len(f_la)):
        if f_la[i] in op_nd:
            if tmp != '': list_f_la.append(tmp)
            tmp = ''
            list_f_la.append(f_la[i])
        else: 
            tmp += f_la[i]
    if tmp != '':list_f_la.append(tmp)
    return list_f_la

def sub_calc_muldiv(f_la):
    f = []
    for i in f_la:
        if i != '(' and i != ')':
            f.append(i)
    i = len(f)-1
    while i >= 0:
        if f[i] == '/': 
            f[i] = float(f[i-1]) / float(f[i+1])
            del f[i+1]
            del f[i-1]
        i-=1
    i = len(f)-1
    while i >= 0:
        if f[i] == '*': 
            f[i] = float(f[i-1]) * float(f[i+1])
            del f[i+1]
            del f[i-1]
        i-=1
    i = len(f)-1
    while i >= 0:
        if f[i] == '-': 
            f[i] = float(f[i-1]) - float(f[i+1])
            del f[i+1]
            del f[i-1]
        i-=1
    i = len(f)-1
    while i >= 0:
        if f[i] == '+': 
            f[i] = float(f[i-1]) + float(f[i+1])
            del f[i+1]
            del f[i-1]
        i-=1
    f = str(f[0])
    return f

def find_sub_form(f_la):
    count = 0           # Количество найденных скобок
    i = 0
    while i < len(f_la):
        if f_la[i] == '(':
            r = i + 1
            while r > i and r < len(f_la):
                if f_la[r] == '(':
                    i = r
                elif f_la[r] == ')':
                    sub_res = sub_calc_muldiv(f_la[i:r+1])
                    del f_la[i+1:r+1]
                    f_la[i] = sub_res
                    i = 0
                    r = 0
                r +=1
        i += 1
    f_la = sub_calc_muldiv(f_la)
    return f_la

resultat = dev_form(formula,operand)
a = find_sub_form(resultat)
print(f'{formula} = {a}')