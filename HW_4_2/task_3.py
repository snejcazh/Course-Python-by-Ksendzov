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
import re


byn_str = input()

if re.search(r'[a-zA-ZА-Яа-я]', byn_str):
    print("Вы ввели не число. Введите число.")
elif not byn_str:
    print("Вы ввели пустое поле. Введите число.")
elif int(byn_str) < 0:
    print("Введите положительное число.")
else:
    byn = int(byn_str)

    print(f'Ты ввёл {byn} byn')
    print(f'Конвертированная сумма в USD = {int(byn / 2.6)}')
    print(f'Конвертированная сумма в EUR = {int(byn / 2.96)}')
    print(f'Конвертированная сумма в CHF = {int(byn / 2.8)}')
    print(f'Конвертированная сумма в GBP = {int(byn / 3.5)}')
    print(f'Конвертированная сумма в CNY = {int(byn / 0.4)}')