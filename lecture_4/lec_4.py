import os
os.system('cls')
# Урок 4. Функции высшего порядка, работа с файлами
# на функции можно ссылаться
# def f(a):
#     return a*a
# a = f
# print (f(3))
# print (a(3))

#task2
# def calk_1(a):
#     return a+a
# def calk_2(a):
#     return a*a
# def math (op, x):
#     print (op(x))

# math (calk_2,3)

# task3 Lambda функция
# в списке хранятся числа. Нужно выбрать только четные числа и составить список пар (число, квадрат сисла)
# [1,2,3,5,8,15,23,38]
# получить [(2,4), (8,64)]
# list_1 = [1,2,3,5,8,15,23,38]
# list_2 = []
# for num in list_1:
#     if num%2 ==0:
#         list_2.append((num, num*num))
        
# print (list_1, list_2)

# терерь через функцию
# def select (f, col):
#     return [f(x) for x in col]

# def where (f, col):
#     return [x for x in col if f(x)]
# def where_2 (f, col):
#     return [x*x for x in col if f(x)]

# list_1 = [1,2,3,5,8,15,23,38]
# res = select (int, list_1)
# print (res)
# res = where (lambda a: a%2==0, res)
# print (res)
# res = where_2 (lambda a: a%2==0, res)
# print (res)
# res = list(select(lambda x: (x, x*x), res))
# print (res)
# ///////////////////////////
# task_3 функция map

# list_1 = [x for x in range(1, 20)]
# print (list_1)

# list_1 = list(map(lambda x: x+10, list_1))
# print (list_1)
# ///////////////

# task_4 С клавиатуры вводится некоторый набор чисел, в качестве разделителя используется пробел. Этот 
# набор чисел будет считан в качестве строки, как превратить List строк в List чисел

# split

# List_1 = input ("введите набор чисел через пробел:  ")
# print (List_1)
# List_1 = list(map(int, List_1.split()))
# print (List_1)
# //////////////////////////////////////

# Работа с файлами

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a') # здесь указываем режим, в котором будем работать
# data.writelines(colors) # разделителей не будет
# data.close()


# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')


# path = 'file.txt'
# data = open('file.txt', 'r')
# for line in data:
#     print(line)
# data.close()

# Мщдуль OS

