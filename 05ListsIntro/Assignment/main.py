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


def common_edge(integers1,integers2):
    first1 = integers1[0]
    first2 = integers2[0]
    last1 = integers1[-1]
    last2 = integers2[-1]
    if first1 == last1 or first1 == last2 or first2 == last1 or first2 == last2:
        result = True
    else:
        result = False
    return result

print(common_edge([1, 2, 4], [4, 5, 6]))

# def all_the_same(1,2,3)