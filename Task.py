"""
1. Открыть файл
2. Сохранить файл
3. Показать все контакты
4. Найти контакт
5. Добавить контакт
6. Изменить контакт
7. Удалить контакт
8. Выход
"""
from mod import *
my_file = "phone_book.txt"
data = []


def main_menu(file, answer = 0):                            
    answer = int(input("Выберите нужный пункт меню: "))
    if answer > 8 or answer <= 0:
        print("такого пункта нет")
    if answer == 8:
        print("Программа окончена")
        return "", answer
    if answer == 3:
        show_all(my_file)
        return "", answer
    if answer == 4:
        search_contakt(data)
        return "", answer
    if answer == 2:
        save_file(my_file, data)
        return "", 8
    if answer == 1:
        return open_file(my_file), answer
    if answer == 5:
        add_contakt(data)
        answer = int(input("Сохранить изменения? Да - 1, нет - 0: "))
        if answer == 1:
            save_file(my_file, data)
            return "", 8
        else:
            return "", 8
    if answer == 6:
        edit_contakt(data, search_contakt(data))
        answer = int(input("Сохранить изменения? Да - 1, нет - 0: "))
        if answer == 1:
            save_file(my_file, data)
            return "", 8
        else:
            return "", 8
    if answer == 7:
        del_contakt(data, search_contakt(data))
        answer = int(input("Сохранить изменения? Да - 1, нет - 0: "))
        if answer == 1:
            save_file(my_file, data)
            return "", 8
        else:
            return "", 8
    return
data = open_file(my_file)                             
while main_menu(my_file)[1] < 8:                        
    main_menu(my_file)



