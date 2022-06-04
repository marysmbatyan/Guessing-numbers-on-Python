#function of number validation
def is_valid(num, n):
    if num.isalpha():
        return False
    if int(num) >= 1 and int(num) <= n:
        return True
    else:
        return False

#start
from random import *
print('Добро пожаловать в числовую угадайку')
n = int(input('Введите верхний диапазон: '))
computer_num = randint(1, n)

#number input
num = input(f'Введите целое число от 1 до {n}: ')
while is_valid(num, n) == False:
    print(f'А может быть все-таки введем целое число от 1 до {n} ?')
    num = input(f'Введите целое число от 1 до {n}: ')
num = int(num)

#comparing
how_many = 1
while num != computer_num:
    if num > computer_num:
        print('Ваше число больше загаданного, попробуйте еще разок')
        how_many += 1
        num = input(f'Введите целое число от 1 до {n}: ')
        while is_valid(num, n) == False:
            print(f'А может быть все-таки введем целое число от 1 до {n} ?')
            num = input(f'Введите целое число от 1 до {n}: ')
        num = int(num)
    elif num < computer_num:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        how_many += 1
        num = input(f'Введите целое число от 1 до {n}: ')
        while is_valid(num, n) == False:
            print(f'А может быть все-таки введем целое число от 1 до {n} ?')
            num = input(f'Введите целое число от 1 до {n}: ')
        num = int(num)
if num == computer_num:
    print('Вы угадали, поздравляем!')

#end    
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
print('Вы сделали', how_many, 'попыток, до того как отгадали')
