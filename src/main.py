from utils import utils


# Стандартизирую данные карты

data_cart = utils.get_list()

# Удаляю пустые словари
for data_operation in reversed(data_cart):
    if len(data_operation) == 0:
        index_empty_element_list = data_cart.index(data_operation)
        del data_cart[index_empty_element_list]

for data_operation in data_cart:
    print(data_operation)