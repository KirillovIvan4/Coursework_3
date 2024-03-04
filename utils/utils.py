import json


def get_list():
    """Функция считывает json файл преобразует его список"""
    with open('../operations.json', 'r', encoding='utf-8') as file:
        data_card = json.load(file)
        return data_card

def get_last_five_operations(data_cart):
    """Функция сортирует список операций по дате и возвращает 5 последних"""
    data_cart.sort(key=lambda dictionary: dictionary['date'])
    return data_cart[-5:]