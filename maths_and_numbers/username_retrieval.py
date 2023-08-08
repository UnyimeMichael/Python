def username_generator(email: str):
    username = email.split("@")[0]
    return f" Your username is {username}"


email = input("Enter email")
# print((username_generator("michaelunyimegodfrey@gmail.com")))
print(username_generator(email))