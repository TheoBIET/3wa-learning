word = "mississipi"
letter = "i"
od = [{l, word.count(l)} for l in set(word)]

def letter_count(w, l):
    return w.count(l)

has_letter = letter_count(word, letter)

print('Il y a', has_letter, letter) if has_letter else print('Il n\'y en a pas')