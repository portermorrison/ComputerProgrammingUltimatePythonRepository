# def make_abc():
#     result = ["a", "b", "c",]
#     return result

# print("abc demonstration:")
# print(make_abc())
# #COMPLETE


# def equal_edges(item):
#     first = item[0]
#     last = item[-1]
#     if first == last:
#         result = True
#     else:
#         result = False
#     return result

# print("equal edges tests:")
# print("[1, 2, 3, 4, 1] -> ", equal_edges([1, 2, 3, 4, 1]))
# print("[5, 6, 7, 8, 9] -> ", equal_edges([5, 6, 7, 8, 9]))
# print("[-1, 0, 1, 2, -1] -> ", equal_edges([-1, 0, 1, 2, -1]))
# print("[4, 4] -> ", equal_edges([4, 4]))
# COMPLETE


# def common_edge(integers1,integers2):
#     first1 = integers1[0]
#     first2 = integers2[0]
#     last1 = integers1[-1]
#     last2 = integers2[-1]
#     if first1 == first2 or first1 == last2 or last1 == first2 or last1 == last2:
#         result = True
#     else:
#         result = False
#     return result

# print(common_edge([1, 2, 4], [4, 5, 6]))
# print(common_edge([1, 2, 4], [7, 7, 7]))
# COMPLETE


# def all_the_same(items):
#     item1,item2,item3 = items
#     if item1 == item2 and item1 == item3:
#         result = True
#     else:
#         result = False
#     return result
# print(all_the_same([1,2,3]))
# print(all_the_same([2,2,2]))
# # COMPLETE


# def all_unique(items):
#     item1,item2,item3 = items
#     if item1 == item2 and item1 == item3:
#         result = False
#     else:
#         result = True
#     return result
# print(all_unique([1,2,3]))
# print(all_unique([2,2,2]))
# # Complete


# def increasing(numbers):
#     num1, num2, num3 = numbers
#     if num1 < num2 and num2 < num3:
#         return True
#     else: 
#         return False

# print(increasing([1,5,9]))
# print(increasing([3, 2, 0]))
# Complete


# def all_true(booleans):
#     tf1, tf2, tf3 = booleans
#     if tf1 == True and tf2 == True and tf3 == True:
#          return True
#     else: 
#         return False
    
# print(all_true([True,False,False]))
# print(all_true([True,True,True]))
# Complete


# def mostly_true(booleans):
#      tf1, tf2, tf3 = booleans
#      if tf1 == True and tf2 == True or tf1 == True and tf3 == True or tf2 == True and tf3 == True:
#        return True
#      else: 
#         return False
    
# print(mostly_true([False,False,False]))
# print(mostly_true([True,True,False]))
# # Complete


# NOTE: Mr Scislowski said it was OK to move onto the next assignment at this point (12/04)