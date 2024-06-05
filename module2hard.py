def get_password(input_stone, all_stones):
    password = ''
    for first_term in range(len(all_stones) - 1):
        for second_term in range(first_term + 1, len(all_stones)):
            if input_stone % (all_stones[first_term] + all_stones[second_term]) == 0:
                password += str(all_stones[first_term]) + str(all_stones[second_term])
    return password


stones = range(1, 20)
first = int(input('Введите число из первого поля: '))
print('Пароль: ', get_password(first, stones))
