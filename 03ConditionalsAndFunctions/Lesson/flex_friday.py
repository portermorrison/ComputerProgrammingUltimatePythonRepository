grade = input("What is your grade this week? ")
tardies = int(input("How many tardies do you have this week? " ))

# comparison operators
# >, >=, <, <=, !=

# long version
# if grade == "F":
#     print("you cannot leave")
# elif grade == "D":
#     print("you cannot leave")
# elif tardies > 0:
#     print("you cannot leave")
# else: 
#     print("you may leave early")

# shorter version
# or, and, not
if grade == "F" or grade == "D" or tardies > 0:
    print("you cannot leave")
else: 
    print("you may leave early")