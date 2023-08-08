def word_index(word: str):
    words = []
    for index, letters in enumerate(word):
        if letters.islower():
            words.append(index)
    return words


word = "EsTHer"
print(word_index(word))
