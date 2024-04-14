# # Урок 3. Списки и словари
# ребуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
# Найдите количество и выведите его.
# list_1 = [1, 2, 3, 4, 5]
# k = 3

# Введите ваше решение ниже

count = 0
for i in list_1:
    if i == k:
        count = count + 1
print (count)

# task_2
# Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
# Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом 
# - выведите его.
# При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения `list_1` и `k`

# При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит 
# разные значения `list_1` и `k` для проверки


# list_1 = [1, 2, 3, 4, 5]
# k = 6

# Введите ваше решение ниже

list_2 =[]
i = 0
while i < len(list_1):
    list_2.append(abs(k - list_1[i]))
    i = i + 1

print (list_1[list_2.index(min(list_2))])

# task_3
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, 
# либо только русские буквы.

# k = "ноутбук"

# Введите ваше решение ниже
eng_glossary = {1:"A, E, I, O, U, L, N, S, T, R", 2:"D, G", 3: "B, C, M, P",
                4:"F, H, V, W, Y", 5:"K", 8:"J, X", 10:"Q, Z"}
rus_glossary = {1:"А, В, Е, И, Н, О, Р, С, Т", 2:"Д, К, Л, М, П, У", 3: "Б, Г, Ё, Ь, Я",
                4:"Й, Ы", 5:"Ж, З, Х, Ц, Ч", 8:"Ш, Э, Ю", 10:"Ф, Щ, Ъ"}
# k = (input ("введите слово: " )).upper()
import string
k = k.upper()
score = 0

for letter in k:
    if letter in string.ascii_uppercase:
        for point, str_letters in eng_glossary.items():
            if letter in str_letters:
                score = score + point
    else:
        for point, str_letters in rus_glossary.items():
            if letter in str_letters:
                score = score + point
print (score)