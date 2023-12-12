import csv

f = open("../data/4000-most-common-english-words.csv", "r")
words = f.read().split("\n")
print(words)
f.close()


f = open("../data/gradebook_data.csv", "r")
reader = csv.reader(f) 
for row in reader:
    print(row)

f.close()