# def is_alliteration(word1, word2):
#     letter1 = word1 [0]
#     letter2 = word2[0]
#     if letter1 == letter2:
#             return True
#     else:
#         return False

# print(is_alliteration("parry", "platapus"))
# #Complete


# def count_vowels(word):
#     vowel_count = 0
#     for letters in word:
#        if letters == "a" or letters == "e"or letters == "i" or letters == "o" or letters == "u":
#            vowel_count = vowel_count + 1
#     return vowel_count

# print(count_vowels("bob"))
# #Complete


# def count_numbers(word):
#     num_count = 0
#     for letter in word:
#         if letter in ["1","2","3","4","5","6","7","8","9","0"]:
#             num_count = num_count +1
#     return num_count
# print(count_numbers("meo0w1ng"))
# #complete


# def count_target_letters(word,target):
#     count = 0
#     for letter in word:
#         if letter == target:
#             count = count + 1
#     return count
# print(count_target_letters("meow", "o"))
# #complete


def in_alphabetical_order(word):
    previous = "a" 
    for letter in word:
        if letter > previous