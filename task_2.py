# Задача 2: Напишите программы создания файла
# добавления в него записей, удаления записей, исправления записей,
# вывода содержимого файла на экран (все описать в функциях)
#
# ------------------------залить все это на github и скинуть мне ссылки

a='Hello\nworld'
def write_f(a):
    with open('text.txt','w') as file:
        file.write(a)
# write_f(a)

def read_f():
    with open('text.txt', 'r') as file:
        r=file.readlines()
    return r
print(read_f())
#

ff=read_f()
b=int(input('Введи 0 или 1'))
def del_el(ff,b):
    del ff[b]  #удалить выбранную строку
    return ff
print(del_el(ff,b))


# del_el()
# print(sd)
# read_f(sd)
# del sd[1]  #удалить выбранную строку
# print(sd)
#
# a=sd[0]  #замена буквы
# print(a)