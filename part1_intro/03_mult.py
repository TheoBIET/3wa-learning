def mult(a, b):
    check = lambda l : type(l) in [list, tuple] and len(l) > 0 and all(type(float(x)) == float for x in l)
    assert check(a) and check(b) and len(a) == len(b)

    s = 0
    for vec in zip(a, b):
        # unpacking pour assigner les valeurs à mes variables
        x, y = vec
        s += float(x) * float(y)

    return s

print(mult([1, 2, 3], [4, 5, 6]))