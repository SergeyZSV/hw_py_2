# Написать программу преобразования десятичного числа в двоичное

print('Введите десятичное число: ', end ='')
n = int(input())

b = ''

while n > 0:
    b = str(n % 2) + b
    n = n // 2

print(f'Десятичное число {n} в двоичной системе равно {b}')