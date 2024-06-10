def single_root_words(root_word, *other_words):
    same_words = []
    root_lower = root_word.lower()
    for x in other_words:
        x_lower = x.lower()
        if x_lower.find(root_lower) != -1 or root_lower.find(x_lower) != -1:
            same_words.append(x)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
