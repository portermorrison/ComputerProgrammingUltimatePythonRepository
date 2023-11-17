def make_pi():
    return [3, 1, 4]

def are_reversed(items1, items2):
    """
    items1: a list of length 3
    items2: a list of length 3
    """
    return items1[0] == items2[2] and items2[0] == items1[2] and items1[1] == items2[1]

def make_repeated_max(items):
    """
    items: list of length 3
    """
    first, second, third = items
    maxVal = max(first, second, third)
    return [maxVal, maxVal, maxVal]

def overwrite_with_max(items):
    """
    items: list of length 3
    """
    first, second, third = items
    maxVal = max(first, second, third)
    items[0] = first
    items[1] = second
    items[2] = third
    return items
