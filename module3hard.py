def calculate_structure_sum(*args, **kwargs):
    sum = 0
    for x in args:
        if isinstance(x, (int, float)):
            sum += x
        elif isinstance(x, str):
            sum += len(x)
        elif isinstance(x, (list, tuple, set)):
            sum += calculate_structure_sum(*x)
        elif isinstance(x, dict):
            sum += calculate_structure_sum(**x)
    for key, value in kwargs.items():
        sum += calculate_structure_sum(key)
        sum += calculate_structure_sum(value)
    return sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
