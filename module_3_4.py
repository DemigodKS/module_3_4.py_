def single_root_words(root_word, *other_words):
    same_words = []

    for word in other_words:
        word = word.casefold()
        root_word = root_word.casefold()
        if word in root_word or root_word in word:
            same_words.append(word)

    return same_words

result1 = single_root_words('Merg','MeRcy', 'merging', 'unmerged', 'Submerge')
print(result1)
result2 = single_root_words('Disablement', 'aBle', 'cheers', 'ABL', 'disable')
print(result2)
result3 = single_root_words('Back', 'ba', 'unBaCk', 'BackYard', 'cheers', 'Backup')
print(result3)
