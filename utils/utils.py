import json


def get_list():
    """Функция считывает json файл преобразует его список"""
    with open('../operations.json', 'r', encoding='utf-8') as file:
        data_card = json.load(file)
        return data_card