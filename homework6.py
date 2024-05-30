my_dict = {'Ася': 2001, 'Оля': 1964, 'Тоня': 1937}
print('Dict:', my_dict)
print('Existing value:', my_dict.get('Ася'))
print('Not existing value:', my_dict.get('Витя'))
my_dict.update({'Витя': 1967, 'Люся': 1939})
print('Deleted value:', my_dict.pop('Тоня'))
print('Modified dictionary:', my_dict)
my_set = {False, 1, 2, 1, 0, 'abc', True, 2==2}
print('Set:', my_set)
my_set.update({5, 6})
my_set.remove(True)
print('Modified set:', my_set)
