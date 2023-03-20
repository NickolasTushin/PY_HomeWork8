def open_file(file):                                        # Открывает файл
    with open(file, "r", encoding="UTF-8") as my_file:
        data = list(map(lambda x: x.upper().split(), my_file.readlines()))
    print("Файл открыт")
    return data

def search_contakt(data: list):                             # Поиск контакта по фамилии, имени, номеру или статусу.
    answer = input("Введите информацию для поиска: ").upper()
    list_index = {}
    count = 1
    for i in range(len(data)):
        if answer in data[i]:
            print(f"{count}. {' '.join(data[i])}")
            list_index[count] = i
            count += 1
    return list_index


def show_all(file):                                         # все контакты
    with open(file, "r", encoding="UTF-8") as my_file:
        print(my_file.read())
    return

def save_file(file, data):                                        # перезаписывает с учетом всех изменений
    with open(file, "w", encoding="UTF-8") as my_file:
        my_file.write("")
    with open(file, "a", encoding="UTF-8") as my_file:

        for i in range(len(data)):
            my_file.writelines(" ".join(data[i]))
            my_file.writelines("\n")
    print("Файл сохранен\nПрограмма окончена")

    return

def add_contakt(data: list):                                    # добавляет контакт
    new_item = input("Введите новый контакт: ФИО номер : ").upper()
    data.append([new_item])
    return data



def edit_contakt(data: list, index: dict):                      # меняет параметры контакта
    item_index = int(input("Введите номер контакта, который нужно изменить:  "))
    param = int(input("Введите параметр, который нужно изменить: фамилия - 1, имя - 2, номер телефона - 3, статус - 4:  "))
    print(f"Прежний параметр: {data[index.get(item_index)][param - 1]}")
    data[index.get(item_index)][param - 1] = input("Введите новое значение: ").upper()
    print(f"Запись измененна {' '.join(data[index.get(item_index)])}")
    return

def del_contakt(data: list, index: dict):                      # удаляет контакт
    item_index = int(input("Введите контакт, который нужно удалить:  "))
    warn = input(f"Вы уверены что хотите удалить контакт {' '.join(data[index.get(item_index)])} (да, нет): ")
    if warn == "да":
        data.pop(index.get(item_index))
        print("Контакт удален")
        return
    if warn == "нет":
        return 8
