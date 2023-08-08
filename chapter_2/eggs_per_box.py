number_of_eggs = int(input("Enter number of eggs: "))
number_of_eggs_in_one_box = 6
number_of_boxes = number_of_eggs // number_of_eggs_in_one_box
number_of_eggs_in_boxes = number_of_boxes * number_of_eggs_in_one_box
eggs_remainder = number_of_eggs % number_of_eggs_in_one_box
space_in_the_box = number_of_eggs_in_one_box - eggs_remainder
print(f"we have {number_of_boxes} boxes filled with {number_of_eggs_in_boxes} eggs and {eggs_remainder} eggs remaining in another box with {space_in_the_box} spaces left in the box")