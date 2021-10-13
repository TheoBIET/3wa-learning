l = ['A', 'B', 'C', 'd', 'E']
d = ['a', 'b', 'c', 'd', 'e']
e = ['A', 'B', 'C', 'D', 'E']

assert all(map(str.isupper, l)) == False
assert all(map(str.isupper, d)) == False
assert all(map(str.isupper, e)) == True
