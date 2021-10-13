nb = -6523

def inversed_int(nb):
    assert type(int(nb)) == int
    return int(str(nb)[::-1]) if nb > 0 else int(str(nb * -1)[::-1]) * -1

print(inversed_int(nb))