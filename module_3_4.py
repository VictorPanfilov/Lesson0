def single_root_words(root_word, *other_words):
    same_words = []
    root_l = root_word.lower()
    for i in other_words:
        if (root_l in i.lower()) or (i.lower() in root_l):
            same_words.append(i)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
