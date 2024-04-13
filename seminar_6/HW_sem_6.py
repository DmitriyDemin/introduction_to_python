# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума).
# На вход подается список с элементамиlist_1 и границы диапазона в виде чисел min_number, max_number.
# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = 0
# max_number = 10

# Введите ваше решение ниже
def search_index(list_1, min_number, max_number):
    for i in range(len(list_1)):
        if list_1[i]>=min_number and list_1[i] <=max_number:
            print (i)

            
search_index(list_1, min_number, max_number)

# task_2
# Заполните массив элементами арифметической прогрессии. Её первый элемент a1 ,
# разность d и количество элементов n будет задано автоматически. Формула для получения 
# n-го члена прогрессии: an = a1 + (n-1) * d.
# a1 = 2
# d = 3
# n = 4

# Введите ваше решение ниже
def list_completion(a1, d, n):
    list_1 = list()
    i = 2
    for i in range(n+1):
        num = a1 + (i-1)*d
        list_1.append(num)
        list_2 = list_1[1:]
  
    for i in range(len(list_2)):
        print (list_2[i])

list_completion(a1, d, n)