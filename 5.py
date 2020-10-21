
my_list = [7, 5, 3, 3, 2]
user_num = int(input('Введите число ... '))
index = 0
for i in my_list:
    if user_num <= i:
        index = my_list.index(i) + 1
my_list.insert(index, user_num)
print(my_list)
