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


# def in_alphabetical_order(word):
#     previous = ""
#     for letter in word:
#         if letter >= previous:
#             pass
#         else:
#             return False
#         previous = letter
#     return True
        
# print(in_alphabetical_order("abbot"))
# print(in_alphabetical_order("sky"))
# #complete


# def alternate_case(word):
#     result = ""
#     previous = "a"
#     for letter in word:
#         if previous.islower():
#             new_letter = letter.upper()
#             result = result + letter.upper()
#         else:
#             new_letter = letter.lower()
#             result = result + letter.lower()
#         previous = new_letter
#     return result

# print(alternate_case("isuckatthis"))
# #complete


# def remove_vowels(word):
#     result = ""
#     for letter in word:
#         if letter in ['a', 'e', 'i', 'o', 'u',]:
#             pass
#         else:
#             result = result + letter
#     return result
 
# print(remove_vowels('meowing'))
# #Completed


# def to_camel_case(phrase):
#     result = ""
#     upper_next = True
#     for unit in phrase:
#         if unit ==  " ":
#             upper_next = True
#             pass
#         elif upper_next == True:
#             result = result + unit.upper()
#             upper_next = False
#         else:
#             result = result + unit
#     return result
# print(to_camel_case('me       ow bron     casuarus            '))
# #Complete


# def to_snake_case(phrase):
#     result = ""
#     for unit in phrase:
#         if unit == " ":
#             result = result + "_"
#         else:
#             result = result + unit
#     return result
# print(to_snake_case("john walmart"))
# #complete


# def without_duplicates(num_list):
#     result = []
#     previous = num_list[0] - 1
#     for unit in num_list:
#         if unit == previous:
#             pass
#         else:
#             result.append(unit)
#         previous = unit
#     return result
# print(without_duplicates([1,2,2,3,4,5,6,6,7,8,8,9]))
# #complete

# def filter_valid_act_scores(scores):
#     valid_scores = []
#     for unit in scores:
#         if unit >0 and unit <37:
#             valid_scores.append(unit)
#         else:
#             pass
#     return valid_scores

# print(filter_valid_act_scores([3, 99, 53, 24, 35]))
# #complete