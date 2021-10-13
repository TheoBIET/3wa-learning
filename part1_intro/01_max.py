l = [0, 1, 100, 4, 9, 16, 25, 36, 49, 64, 81]


def max(l):
    assert type(l) == list and len(l) > 0
    max = l[0]
    for num in l:
        if (num > max):
            max = num
    return max


lMax = max(l)

print("Max:", lMax, "\nIndex:", l.index(lMax))  # Max: 100
                                               # Index: 2