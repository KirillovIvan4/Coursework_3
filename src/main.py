from utils import utils


# Стандартизирую данные карты

data_cart = utils.get_list()

# Удаляю пустые словари
for data_operation in reversed(data_cart):
    if len(data_operation) == 0:
        index_empty_element_list = data_cart.index(data_operation)
        del data_cart[index_empty_element_list]

# Удаляю отмененые операции
for data_operation in reversed(data_cart):
    if data_operation["state"] == "CANCELED":
        index_empty_element_list = data_cart.index(data_operation)
        del data_cart[index_empty_element_list]

for data_operation in data_cart:
    # Удаляю "Т" в дате
    data_operation['date'] = data_operation['date'].replace('T',' ')
    # Оставляю только дату и время
    data_operation['date'] = data_operation['date'][:19]

# Получаем последние 5 операций
last_five_operations_cart = utils.get_last_five_operations(data_cart)
# форматирую дату
last_five_operations_cart = utils.formation_date(last_five_operations_cart)

for data_operation in last_five_operations_cart:
    print(data_operation)