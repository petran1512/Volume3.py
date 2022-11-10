# 4) Can you update (3) to make it so that if a validation fails then rather than terminating
# the program, the user is given a chance to enter correct data? (but the error message is still shown).

name = input("Enter your name: ")
age = int(input("Enter your age: "))
flag_letter = False
flag_number = False
for i in name:
    if i.isalpha() >=1:         #**for not all but only for one**
        flag_letter = True
    else:
        print("Error wrong data.")
        name = input("Enter your name: ")
    if 0 < age <= 150:
        flag_number = True
    else:
        print("Error wrong data.")
        age = int(input("Enter your age: "))
if flag_letter and flag_number == True:
    print("Hello, " + name + " you are " + str(age) + " years old!")