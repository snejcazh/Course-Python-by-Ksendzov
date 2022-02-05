# 1) Создать переменную типа String
# 2) Создать переменную типа Integer
# 3) Создать переменную типа Float
# 4) Создать переменную типа Bytes
# 5) Создать переменную типа List
# 6) Создать переменную типа Tuple
# 7) Создать переменную типа Set
# 8. Создать переменную типа Frozen set
# 9) Создать переменную типа Dict

nstring = 'Строка'
ninteger = 3
nfloat = 3.3
nbytes = bytes(4)
nlist = [2, 1, 'd']
ntuple = (2, 4)
nset = {2, 4, 1}
nfrozenset = frozenset(nlist)
ndict = {1: ntuple, 2: nbytes, 3: ninteger}

# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.

list = [nstring, ninteger, nfloat, nbytes, ntuple, nset, nfrozenset, ndict]
for item in list:
    print(f'Значение переменной - {item}, тип данных - {type(item)}')

print('--------------------------------------')

# 11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
string1 = "Первая строка"
string2 = "Вторая строка"
stringall = string1 + " " + string2

print(stringall)

print('--------------------------------------')

# 12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
print(nstring, ninteger)

print('--------------------------------------')
# 13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
print(nstring + str(ninteger))