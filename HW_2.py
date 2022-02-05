import math


# Arithmetic
#
#  1. Создать переменную item_1 типа integer.
#  2. Создать переменную item_2 типа integer.
item_1 = 64
item_2 = 4

#  3. Создать переменную result_sum в которой вы суммируете item_1 и item_2.
#  4. Вывести result_sum в консоль.
result_sum = item_1 + item_2
print(f'Сумма = {result_sum}')

#  5. Создать переменную result_subtr в которой вы вычитаете большую по значению переменную из меньшей по значению.
#  6. Вывести result_subtr в консоль.
result_subtr = item_1 - item_2
print(f'Разница = {result_subtr}')

#  7. Создать переменную result_multi в которой вы умножаете item_1 на item_2.
#  8. Вывести result_multi в консоль.
result_multi = item_1 * item_2
print(f'Произведение = {result_multi}')

#  9. Создать переменную result_exp в которой вы item_1 возводите в степень item_2.
#  10. Вывести result_exp в консоль.
result_exp = item_1 ** item_2
print(f'{item_1} в степени {item_2} = {result_exp}')

#  11. Создать переменную result_m_exp в которой вы item_1 возводите в степень item_2 используя библиотеку math.
#  12. Вывести result_m_exp в консоль.
result_m_exp = math.pow(item_1, item_2)
print(f'{item_1} в степени {item_2} = {result_m_exp}')

#  13. Создать переменную result_s_root в которой вы найдёте квадратный корень любой из переменной item
#  14. Вывести result_s_root в консоль.
result_s_root = item_1 ** 0.5
print(f'Квадратный корень из {item_1} = {result_s_root}')

#  15. Создать переменную result_m_s_root в которой вы найдёте квадратный корень любой из переменной item используя библиотеку math.
#  16. Вывести result_m_s_root в консоль.
result_m_s_root = math.sqrt(item_1)
print(f'Квадратный корень из {item_1} = {result_m_s_root}')

#  17. Создать переменную result_mp_s_root в которой вы найдёте квадратный корень любой из переменной item используя библиотеку math используя метод pow.
#  18. Вывести result_mp_s_root в консоль.
result_mp_s_root = math.pow(item_1, 0.5)
print(f'Квадратный корень из {item_1} = {result_mp_s_root}')

print('----------------------------------')
#  19. Присвоить переменной item_1 odd значение
#  20. Присвоить переменной item_2 even значение
item_1 = 49
item_2 = 32

#  21. Создать переменную result_division в которой вы разделите item_1 на item_2.
#  22. Вывести result_division в консоль.
result_division = item_1 / item_2
print(f'Частное = {result_division}')

#  23. Создать переменную result_m_floor и result_division округлить до ближайшего целого меньшего чем result_division.
#  24. Вывести result_m_floor в консоль.
result_m_floor = math.floor(result_division)
print(f'Частное, округленное в меньшую сторону = {result_m_floor}')

#  25. Создать переменную result_m_ceil и result_division округлить до ближайшего целого большего чем result_division.
#  26. Вывести result_m_ceil в консоль.
result_m_ceil = math.ceil(result_division)
print(f'Частное, округленное в большую сторону = {result_m_ceil}')

#  27. Создать переменную result_int и result_division округлить до ближайшего целого через явное приведение.
#  28. Вывести result_int в консоль.
result_int = int(result_division)
print(f'Округленное частное = {result_int}')

#  29. Создать переменную result_no_division_loss в которой вы разделите item_1 на item_2 без остатка.
#  30. Вывести result_no_division_loss в консоль.
result_no_division_loss = item_1 // item_2
print(f'Деление без остатка = {result_no_division_loss}')

#  31. Создать переменную result_division_loss в которой вы найдёте остаток от деления item_1 на item_2.
#  32. Вывести result_division_loss в консоль.
result_division_loss = item_1 % item_2
print(f'Остаток от деления = {result_division_loss}')

print('----------------------------------')
# Дальше будет реализация через арифметические действия с присваиванием.
#
#  33. Создать переменную item_3 и присвоить ей целое число
#  34. Прибавить 10 к item_3 с присвоением.
#  35. Вывести item_3 в консоль.
item_3 = 5
item_3 += 10
print(f'item_3 + 10 = {item_3}')

#  36. Отнять 5 от item_3 с присвоением.
#  37. Вывести item_3 в консоль.
item_3 -= 5
print(f'item_3 - 5 = {item_3}')

#  38. Умножить item_3 на 3 с присвоением.
#  39. Вывести item_3 в консоль.
item_3 *= 3
print(f'item_3 * 3 = {item_3}')

#  40. Разделить item_3 на 2 с присвоением.
#  41. Вывести item_3 в консоль.
item_3 /= 2
print(f'item_3 / 2 = {item_3}')

#  42. Возвести в степень 2 item_3 с присвоением.
#  43. Вывести item_3 в консоль.
item_3 **= 2
print(f'item_3 в квадрате = {item_3}')

#  44. Найти квадратный корень item_3 с присвоением.
#  45. Вывести item_3 в консоль.
item_3 **= 0.5
print(f'Квадратный корень из item_3 = {item_3}')

#  46. Присвоить остаток от деления item_3
#  47. Вывести item_3 в консоль.
item_3 %= 4
print(f'Остаток от деления на 4 = {item_3}')

print('----------------------------------')
# Boolean
#
#  48. Создать переменную b_item_t и присвоить True
#  49. Создать переменную b_item_f и присвоить False
b_item_t = True
b_item_f = False

#  50. Создать переменную b_item_relult_sum и присвоить сумму b_item_t и b_item_f
#  51. Вывести b_item_relult_sum в консоль.
b_item_result_sum = b_item_t + b_item_f
print(f'Сумма = {b_item_result_sum}')

#  52. Создать переменную b_item_relult_subtr и присвоить разницу b_item_t и b_item_f
#  53. Вывести b_item_relult_subtr в консоль.
b_item_result_subtr = b_item_t - b_item_f
print(f'Разница = {b_item_result_subtr}')

#  54. Создать переменную b_item_relult_multi и присвоить умножение b_item_t и b_item_f
#  55. Вывести b_item_relult_multi в консоль.
b_item_result_multi = b_item_t * b_item_f
print(f'Произведение = {b_item_result_multi}')

#  56. Создать переменную b_item_relult_division и присвоить деление b_item_t и b_item_f
#  57. Вывести b_item_relult_division в консоль. (Получить ошибку)

# Следующие 2 строки нужно раскомментить для получения ошибки
# b_item_result_division = b_item_t / b_item_f
# print(f'Частное = {b_item_result_division}')

#  58. Создать переменную b_item_1_int и присвоить явное приведение b_item_t к int
#  59. Вывести b_item_1_int в консоль.
b_item_1_int = int(b_item_t)
print(f'{b_item_t} в int = {b_item_1_int}')

#  60. Создать переменную b_item_2_int и присвоить явное приведение b_item_f к int
#  61. Вывести b_item_2_int в консоль.
b_item_2_int = int(b_item_f)
print(f'{b_item_f} в int = {b_item_2_int}')