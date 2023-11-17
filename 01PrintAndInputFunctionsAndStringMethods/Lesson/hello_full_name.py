print("Please enter your first name")
first = input()
firstStripped = first.strip().capitalize()

print("Please enter your last name")
last = input()
lastStripped = last.strip().capitalize()

print("Please enter your nickname")
nick = input()
nickStripped = nick.strip().capitalize()

# using three arguments
print("Hello", firstStripped, lastStripped, "or should I say", nickStripped)

# # use joining strings
# message = "Hello " + first + " " + last + " or should I say " + nick
# print(message)