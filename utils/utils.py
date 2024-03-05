import json
from datetime import date

def get_list():
    """Функция считывает json файл преобразует его список"""
    with open('../operations.json', 'r', encoding='utf-8') as file:
        data_card = json.load(file)
        return data_card


def get_last_five_operations(data_cart):
    """Функция сортирует список операций по дате и возвращает 5 последних"""
    data_cart.sort(key=lambda dictionary: dictionary['date'])
    return data_cart[-5:]


def formation_date(last_five_operations_cart):
    """Функция форматирует дату под требования задния"""
    for operations in last_five_operations_cart:
        operations["date"] = operations["date"][:10]
        date_operations = date.fromisoformat(operations['date'])
        operations['date'] = date_operations.strftime("%d.%m.%Y")
    return last_five_operations_cart