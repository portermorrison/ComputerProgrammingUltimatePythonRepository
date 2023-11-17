# input captures strings... we want to treat them as numbers
x = float(input("Please enter x"))
y = float(input("Please enter y"))
print("Their sum is")
print(x + y)

print("Their rounded sum is: ")
print(round(x + y))

print("Their sum rounded to 2 decimal places is: ")
print(round(x + y, 2))