phrase = "Hello world"
phrase_1 = "welcome to python environment"
print(phrase[-11])
print(phrase +", "+ phrase_1)
x = "bazinga"
print(x[2:6])

user_input = input("""Enter name:
""")
final_index = len(user_input) - 1
half_of_final_index = (final_index) // 2
last_character = user_input[final_index]
first_character = user_input[0]
print(first_character)
print(user_input[half_of_final_index])
print(last_character)
print(half_of_final_index)
print(final_index)
print(user_input[0:])
print(user_input[::-1])
print(user_input[:half_of_final_index])
print(user_input[half_of_final_index:])
print(user_input[half_of_final_index::-1])
print(user_input[:half_of_final_index:-1])