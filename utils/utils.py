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


def add_from_in_operations(last_five_operations_cart):
    """Функция проверян наличее срета отправителя и обавляет ключ from и значение 'Отсутствует' если такого ключа нет"""
    for operations in last_five_operations_cart:
        if len(operations) == 6:
            operations["from"] = "Отсутствует"
    return last_five_operations_cart


def disguise_sender_account(last_five_operations_cart):
    """Функция маскерует номер счета отправителя отображая первые 6 цифр и последние 4 цифры"""
    for operations in last_five_operations_cart:
        if operations["from"] != "Отсутствует":
            operations["from"] = operations["from"][:-10] + "*" * 6 + operations["from"][-4:]
    return last_five_operations_cart


def disguise_recipients_account(last_five_operations_cart):
    """Функция маскерует номер счета получателя отображая только последние 4 цифры"""
    for operations in last_five_operations_cart:
        operations["to"] = operations["to"][:5] + "**" + operations["to"][-4:]
    return last_five_operations_cart