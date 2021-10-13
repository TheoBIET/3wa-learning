matrix = [[1,2,3],[4,5,6],[7,8,9]]

def dimension(m):
    n = len(m)
    assert n > 0
    p = len(m[0])
    assert p > 0
    for r in m:
        assert len(r) == p
    return (n, p)

def transpose (m):
    n, p = dimension(m)
    return [[m[j][i] for j in range(n)] for i in range(p)]

transposed = transpose(matrix)

assert matrix == [[1,2,3],[4,5,6],[7,8,9]]
assert transposed == [[1,4,7], [2,5,8], [3,6,9]]

print(transposed)
