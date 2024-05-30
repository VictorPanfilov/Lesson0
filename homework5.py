immutable_var = (1, 'Привет', True, [1, 2, 3])
print('Immutable tuple:', immutable_var)
# immutable_var[1] = 2
#     immutable_var[1] = 2
#     ~~~~~~~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment
# Почему нельзя изменить значения элементов кортежа?
# Потому что кортеж относится к неизменяемому типу данных.
mutable_list = [1, 'Привет', True, [1, 2, 3]]
mutable_list[1] = 2
print('Mutable list:', mutable_list)