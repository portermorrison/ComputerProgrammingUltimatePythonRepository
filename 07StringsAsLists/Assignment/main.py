# def is_alliteration(word1, word2):
#     letter1 = word1 [0]
#     letter2 = word2[0]
#     if letter1 == letter2:
#             return True
#     else:
#         return False

# print(is_alliteration("parry", "platapus"))
# #Complete
def count_vowels(word):
    vowel_count = 0
    for vowels in word:
       if vowels == "a" or "e"or "i" or "o" or "u":
           vowel_count = vowel_count + 1
    return vowel_count

print(count_vowels())

