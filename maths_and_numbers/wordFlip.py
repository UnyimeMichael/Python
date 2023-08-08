name = input("Enter a word: ")
name = name.lower()
flipx = name[::-1]
if name == flipx:
    print("True; This is a Palindrome")
else:
    print("false; This is not a Palindrome")



