# 2) Update the program in (1) to validate that the user’s name contains at least one character and
# the user’s age is greater than 0. If either validation fails exit the program and print
# an error message to the user

name = input("Enter your name: ")
age = int(input("Enter your age: "))
flag_letter = False
flag_number = False
for i in name:
    if i.isalpha():
        flag_letter = True
    # else:
    #print("Error Error!!!")
    if age > 0:
        flag_number = True
# else:
#     print("Wrong age...age must be greater than 0.")
if flag_letter and flag_number == True:
    print("Hello, " + name + " you are " + str(age) + " years old!")
else:
    print("Error wrong data.")
    print("These are wrong data please try again")
    print("Try something again:”)