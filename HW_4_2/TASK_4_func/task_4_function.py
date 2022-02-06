
import re


def inputdata():
    currency = input("Выберите валюту из ['USD','EUR','CHF','GBP','CNY'] ")
    sum_str = input("Введите сумму ")
    return currency, sum_str


def validation(currency, sum_str):
    if re.search(r'[a-zA-ZА-Яа-я]', sum_str):
        print("Вы ввели не число. Введите число.")
    elif not sum_str:
        print("Вы ввели пустое поле. Введите число.")
    elif int(sum_str) < 0:
        print("Введите положительное число.")
    else:
        conversion(currency, sum_str)


def conversion(currency, sum_str):
    sum = int(sum_str)

    print(f'Вы ввели сумму {sum} и валюту {currency}')
    if currency == 'USD':
        print(f'Конвертированная сумма в USD = {int(sum / 2.6)}')
    elif currency == 'EUR':
        print(f'Конвертированная сумма в EUR = {int(sum / 2.96)}')
    elif currency == 'CHF':
        print(f'Конвертированная сумма в CHF = {int(sum / 2.8)}')
    elif currency == 'GBP':
        print(f'Конвертированная сумма в GBP = {int(sum / 3.5)}')
    elif currency == 'CNY':
        print(f'Конвертированная сумма в CNY = {int(sum / 0.4)}')
    else:
        print(f'Мы не знаем курс конвертации в {currency}')
