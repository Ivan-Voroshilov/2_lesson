
user_string = input('Введите строку из нескольких слов разделённых пробелом ... ')
user_list = user_string.split()
# print(user_list) # Проверяем список
for i in user_list:
    print(f'{user_list.index(i) + 1} - {i[:10]}')
