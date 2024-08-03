def print_params(a=1, b='строка', c=True):
    print(a, b, c)
    return


# print_params() 1 строка True
# print_params(6) 6 строка True
# print_params(6, 7) 6 7 True
# print_params(6, 7, 8) 6 7 8
# print_params(b = 25) 1 25 True
# print_params(c = [1,2,3]) 1 строка [1, 2, 3]

# values_list = [0, ('abc', 5), {1, 4, 2}]
# values_dict = {'a': 8, 'b': [1, 2, 3], 'c': {'qw': 1, 'er': 3}}
# print_params(*values_list) 0 ('abc', 5) {1, 2, 4}
# print_params(**values_dict) 8 [1, 2, 3] {'qw': 1, 'er': 3}

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
