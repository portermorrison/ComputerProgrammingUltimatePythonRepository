# def count_failing_grades(grades):
#     num_of_failing = 0
#     for grade in grades:
#         if grade < 60:
#             num_of_failing =  num_of_failing + 1
#     return num_of_failing

# print(count_failing_grades([50,30,80]))
# COMPLETE


# def count_act_scores(scores):
#     valid_score_count = 0
#     for score in scores:
#         if score >0 and score <37:
#             valid_score_count = valid_score_count + 1
#     return valid_score_count
# print(count_act_scores([300,21,0,58,30]))
# #Complete


# def number_sum(nums):
#     total = 0
#     for num in nums:
#         total = total + num
#     return total

# print(number_sum([1, 1, 5, 2]))

# #complete


# def average_act_score(nums):
#     valid_count = 0
#     total = 0
#     for num in nums:
#         if num < 37 and num > 0:
#             valid_count = valid_count + 1
#             total = num + total 
            
#     if valid_count == 0:
#         return None
    
#     mean = total/valid_count
#     return mean
# # complete


# def all_true(booleans):
#     for boolean in booleans:
#         if boolean == True:
#             pass
#         else:  
#             return False
#     return True

# print(all_true([True, True, True]))
# print(all_true([True, True, True, True, False, True]))def mostly true


# def mostly_true(booleans):
#     boolean_true = 0
#     boolean_false = 0
#     for boolean in booleans:
#         if boolean == True:
#             boolean_true = boolean_true + 1
#         else: 
#             boolean_false = boolean_false + 1
    
#     if boolean_true > boolean_false:
#         return True
#     else:
#         return False
# #Complete


# def has_vowel(letters):
#     is_vowel = 0
#     non_vowel = 0
#     for letter in letters:
#         if letter not in ["a","e","i","o","u"]:
#             pass
#         else:
#             return True
#     return False

# print(has_vowel(["f", "f", "f","f","o"]))        
# print(has_vowel(["f", "f", "f", "f"]))
# #Complete