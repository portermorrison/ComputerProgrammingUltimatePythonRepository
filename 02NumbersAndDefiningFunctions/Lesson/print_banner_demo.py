def print_separator(section_name):
    print("".center(80, "*"))
    print(section_name.center(80))
    print("".center(80, "*"))

# personal info
print_separator("personal info")

name = input("please enter your name: ")
age = int(input("please enter your age: "))

# class details
print_separator("class details")

block1 = input("please enter the class you have block 1: ")
block2 = input("please enter the class you have block 2: ")
block3 = input("please enter the class you have block 3: ")
block4 = input("please enter the class you have block 4: ")

# favorite things
print_separator("favorite things")

color = input("please enter your favorite color: ")
animal = input("please enter your favorite animal: ")

