num = 3

if num >= 0:
    print('Число больше либо равно 0')
else:
    print('Число отрицательное')


str_1 = 'test'
str_2 = 'test1'

if (str_1 in str_2):
    print('Да')
else:
    print('Нет')


num_float = 3.4

if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Число отрицательное')


permit_print = True

if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')


a = 2

if a > 0 and a <= 4:
    print('бакалавр')
elif a >=5 and a <= 6:
    print('магистр')
elif a >= 7 and a <= 9:
    print('аспирант')
else:
    print('Введите корректный год обучения')