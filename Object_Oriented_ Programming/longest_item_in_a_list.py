def letter(word):
    word = " "
    for word in word[1::]:
        if word[0] in word == word[1::]:
            word[1::].append("$")
            return word


w = "restart"
print(letter(w))
