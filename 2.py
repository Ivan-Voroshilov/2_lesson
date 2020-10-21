
string_1 = input('Введите значения списка через пробел (без одинаковых значений) ...')
# print(type(string_1)) # Проверяю что строка
list_1 = string_1.split()
# print(type(list_1)) # Проверяю что список
print(f'Ваш заданный список  -  {list_1}')
list_2 = []  # Пустой для заполнения в него итогового списка
for i in list_1:
    if list_1.index(i) % 2 == 0:
        list_2.insert(list_1.index(i)+1, i)
    else:
        list_2.insert(list_1.index(i)-1, i)
print(f'Ваш измененный список - {list_2}')
