# 1) Create a program that reads the user’s name and age (in two separate lines with
# the appropriate prompt each time) and prints out the string: Hello, {name} you are {age} years old!

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello, " + name + " you are " + str(age) + " years old!”)