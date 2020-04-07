int(12.5) # сделать целым числом.
'слово'.encode() # b'\xd1\x81\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xbe'
b'\xd1\x81\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xbe'.decode() # показать слово.

user = input('Введите значение: ') # Ожидание ввода
print(type(user)) # Узнать тип введённого значения.

x, y = map(int, input().split())
print(type(x))
print(x, y) # Вывести сразу 2 значения типа int.

rav = 'toyota'
isinstance(rav, str) # Является ли rav строкой?
id(rav) # Узнать id
type(rav) # Узнать тип переменной.
rav.find('y') # Узнать номер буквы.
rav.upper() # Всё капсом.
rav.lower() # Всё маленькими.
rav.isalpha() # Все ли в строке буквы.
rav.numeric() # Все ли цифры.
rav.replace('y', 'Y') # замена буквы.
print(rav)

my_list = [1,2,3,4,5] # Список.

my_list.extend([7,4,1]) # Расширить список или my_list + [7,4,1]
my_list.append(100) # добавить новое значение в конец списка
my_list.insert(3, 'abc') # добавить строку к списку на 3 место.
del my_list[3] # Удалить данные под номером 3 из списка.
my_list.remove(4) # Удалить первую попавшуюся четвёрку.
5 in my_list # Входит ли значение 5 в список.
my_list.count(4) # Узнать сколько четвёрок в списке.
min(my_list) # минимальное значение в списке/
my_list.sort() # Сортировать список.

matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix[1][1]

range(0,100) # Создать список с заполнением от 0 до 100.
list(range(50)) # Показать первые 50 значений списка.

my_tuple = (1,2,3) # Создание картеж
