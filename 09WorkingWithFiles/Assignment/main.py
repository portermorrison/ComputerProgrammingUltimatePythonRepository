import csv
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


f = open("../data/4000-most-common-english-words.csv", "r")
words = f.read().split("\n")
f.close()

def count_vowels(word):
    num_of_vowels = 0
    for letters in word:
        if letters in ["a", "e", "i", "o", "u",]:
            num_of_vowels = num_of_vowels +1
    return num_of_vowels

        
print(count_vowels("hairline"))
print(count_vowels("rabbit"))


def find_most_vowels(wordlist):
    max_count = 0
    winning_word = ""
    for word in wordlist:
        num_vowels = count_vowels(word)
        # if the current word has more vowels than the winning word...
        if num_vowels > max_count:
            max_count = num_vowels
            winning_word = word
    return winning_word
