str_list = input("Введите символы через пробел: ").split()
#print(str_list)

new_str = []
for s in str_list:
    if len(s) <= 3:
        new_str.append(s)

print("Массив строк длиной не больше 3 символов:")
print(new_str)