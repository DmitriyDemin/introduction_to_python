import os
os.system('cls')
# Работа с файлами

# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.

contact_data = {
    'first_name': None,
    'second_name': None,
    'pater_name': None,
    'phone_number': None,
    'birthday': None,
    'comment': None
}

def ask_data():
    s_name = input("Введите фамилию: ")
    f_name = input("Введите имя: ")
    m_name = input("Введите отчество: ")
    phone = input("Введите номер телефона: ")
    contact = {'second_name': s_name,
    'first_name': f_name,
    'middle_name': m_name,
    'phone_number': phone}
    return contact

def add_new_contact():
# if not check_data(contact):
# return False
    contact = ask_data()
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        for value in contact.values():
            file.write(value, delimiter=';')
            file.write('\n')
            
    return True

add_new_contact()

# def open_phonebook():
# title = ["Фамилия", "Имя", "Отчество", "Телефон"]
# with open('phonebook.txt', 'r', encoding='utf-8') as file:
# print("\t\t".join(title))
# for line in file:
# print("\t\t".join(line.split(";")))
# # print(line.split(";"), end="\t")

# def find_contact():
# print(f"Поиск по:\n1 имени\n2 фамилии\n3 отчеству\n4 номеру\n0 выход")
# s_name = input("Введите фамилию: ")
# with open('phonebook.txt', 'r', encoding='utf-8') as file:
# for line in file:
# if s_name in line:


# def main():
# isStop = 10
# while isStop != 0:
# print(f"Выберете что хотите сделать:\n1 найти\n2 добавить\n3 сохранить\n4 открыть всю книгу\n5 копирование\n0 выход")
# isStop = int(input(">"))
# if isStop == 1:
# find_contact()
# elif isStop == 2:
# add_new_contact()
# elif isStop == 4:
# open_phonebook()
# input("Нажмите Enter чтобы продолжить")
# main()
# # Николай Судьев Иванов; Иван; Иванович; 123456;
# # Петров; Петр; Петрович; 234567;
# # Сидоров; Сидр; Сидорович; 345678;
# # Игнатов; Игнат; Игнатович; 654321;
# # Смирнов; Иван; Петрович; 222222;
# # Кузнецов; Петр; Игнатович; 333333;
# # Соколов; Игнат; Васильевич; 456127;
# # Попов; Василий; Леонович; 897897;
# # Жуков; Сидр; Иванович; 012348;