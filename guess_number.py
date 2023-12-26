import random as r

number = r.randint(1, 100)
print(number)

while True:
    our_number = int(input('Введите число:'))
    if our_number == number:
        print('Отличная интуиция! Вы угадали число :)')
        break
    elif our_number < number:
        print('Ваше число меньше того, что загадано')
    else:
        print('Ваше число больше того, что загадано')