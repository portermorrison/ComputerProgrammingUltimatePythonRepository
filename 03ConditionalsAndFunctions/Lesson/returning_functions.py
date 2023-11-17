def is_valid_sat_score(number):
    if number >= 200 and number <= 800:
        return True
    else:
        return False

print("is_valid_sat_score")
print("150 => ", is_valid_sat_score(150))
print("450 => ", is_valid_sat_score(450))
print("800 => ", is_valid_sat_score(800))
print("810 => ", is_valid_sat_score(810))


def is_pythagorean_triple(n1, n2, n3):
    a = min(n1, n2, n3)
    c = max(n1, n2, n3)

    b = n1 + n2 + n3 - a - c

    if pow(a, 2) + pow(b, 2) == pow(c, 2):
        return True
    else:
        return False

print("is_pythagorean_triple")
print("3, 4, 5 => ", is_pythagorean_triple(3, 4, 5))
print("3, 4, 7 => ", is_pythagorean_triple(3, 4, 7))
print("5, 4, 3 => ", is_pythagorean_triple(5, 4, 3))


    