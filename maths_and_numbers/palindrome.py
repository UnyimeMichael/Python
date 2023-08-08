def palindrome(lzt):
    if lzt.lower() == lzt.lower()[::-1]:
        return f"True, its a palindrome"
    else:
        return f"False, its not a palindrome"


lzt = input("Enter a name: ")
print(palindrome(lzt))