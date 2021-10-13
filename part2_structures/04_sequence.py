l = [1,3,7,8,9,1,2,3,8]
s = [1, 2, 3]
w = 'HELLO, JE TESTE'
sw = 'JE T'

def search_sequence(l, s):
    return [(i, i+len(s)) for i in range(len(list(l))) if l[i:i+len(s)] == s]

print(search_sequence(l, s))
print(search_sequence(w, sw))