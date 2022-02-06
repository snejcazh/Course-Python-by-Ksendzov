# Задача №3 Обменник.
# Создать скрипт который будет запускаться из консоли 1 раз, выдавать результат и закрываться.
#     1.На вход обменнику вводишь количество денег int.
#     2. На выходе в консоль выводится ответ в таком виде:
#         "Ты ввёл int (Валюта)"
#         "конвертированная сумма в USD = int"
#         "конвертированная сумма в EUR = int"
#         "конвертированная сумма в CHF = int"
#         "конвертированная сумма в GBP = int"
#         "конвертированная сумма в CNY = int"
#     3. Скипт должен выдать сообщение
#         "Введите положительное число."
#     Если число меньше 0.
#         "Вы ввели не число. Введите число."
#     Если введены буквы.
#         "Вы ввели пустое поле. Введите число."
#     Если введено пустое значение.
#     4. Валюту пользователя определите сами.

def validation(line):
    if not line:
        print("Вы ввели пустое поле. Введите число.")
    elif notnumber(line):
        print("Вы ввели не число. Введите число.")
    elif int(line) < 0:
        print("Введите положительное число.")
    else:
        konvertprint(line)

def notnumber(line):
    try:
        int(line)
        return False
    except ValueError:
        return True

def konvertprint(sum_str):
    sum = int(sum_str)
    print(f'Ты ввёл {sum} byn')
    print(f'"Конвертированная сумма в USD = {int(sum / 2.6)}')
    print(f'"Конвертированная сумма в EUR = {int(sum / 2.96)}')
    print(f'"Конвертированная сумма в CHF = {int(sum / 2.8)}')
    print(f'"Конвертированная сумма в GBP = {int(sum / 3.5)}')
    print(f'"Конвертированная сумма в CNY = {int(sum / 0.4)}')


byn_str = input()
validation(byn_str)