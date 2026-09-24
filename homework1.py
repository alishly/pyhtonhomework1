import random
import math

while True:

    length = int(input('Длина пароля 6-20: '))
    while length < 6 or length > 20:
        length = int(input('Длина неверна, попробуйте еще раз: '))

    low = 'abcdefghijklmnopqrstuvwxyz'
    up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    special = '!@#$%^&*'

    chars = ''
    types = 0
    required = ''


    if input('Включить строчные? (да/нет): ') == 'да':
        chars += low
        types += 1
        required += random.choice(low)

    if input('Включить заглавные? (да/нет): ') == 'да':
        chars += up
        types += 1
        required += random.choice(up)

    if input('Включить цифры? (да/нет): ') == 'да':
        chars += digits
        types += 1
        required += random.choice(digits)

    if input('Включить спецсимволы? (да/нет): ') == 'да':
        chars += special
        types += 1
        required += random.choice(special)


    if types == 0:
        print('Нужно выбрать хотя бы одну категорию! ')
        continue


    password = required
    while len(password) < length:
        password += random.choice(chars)


    mix = ''
    while password:
        i = random.randint(0, len(password) - 1)
        mix += password[i]
        password = password[:i] + password[i + 1:]
    password = mix


    entropy = math.log2(len(chars) ** length)


    if entropy < 30:
        strength = 'Очень слабый'
    elif entropy < 50:
        strength = 'Слабый'
    elif entropy < 70:
        strength = 'Средний'
    elif entropy < 90:
        strength = 'Хороший'
    else:
        strength = 'Отличный'


    print('Сгенерированный пароль: ' + password)
    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print('Длина: ' + str(length) + ' символов')
    print('Категорий: ' + str(types) + ' из 4')
    print('Энтропия: ' + str(round(entropy, 2)) + ' бит')
    print('Надёжность: ' + strength)
    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

    if input('Сгенерировать ещё? (да/нет): ') != 'да':
        print('Программа завершена.')
        break