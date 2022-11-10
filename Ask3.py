# 3) Update the program in (2) to also validate that the age is not greater than 150.

name = input("Enter your name: ")
age = int(input("Enter your age: "))
name_has_char = False
age_is_valid = False
for i in name:
    if i.isalpha() >= 1:     # **must be for all not just for one **
        name_has_char = True
if 0 < age <= 150:
    age_is_valid = True
if not name_has_char and age_is_valid:
    print("Hello, " + name + " you are " + str(age) + " years old!")
else:
    print("Error wrong data.”)