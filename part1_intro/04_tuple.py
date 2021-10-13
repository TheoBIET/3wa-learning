def sumTuple(a, b):
    check = lambda l : type(l) in [list, tuple] and len(l) > 0 and all(type(float(x)) == float for x in l)
    assert check(a) and check(b) and len(a) == len(b)

    res = 0
    old = 1

    for vec in zip(a, b):
        x, y = vec
        cur = float(x) + float(y)
        res += (cur * old)
        old = cur

    return res

tup = ((1, 2), (3, 4))
wanted = (tup[0][0] + tup[1][0]) + ((tup[0][0] + tup[1][0]) * (tup[0][1] + tup[1][1]))
result = sumTuple((1, 2), (3, 4))

assert result == wanted