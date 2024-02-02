# Fast modular exponentiation (b, e, m) that computes b^e mod m
# using around 2log base 2 modular multiplications.

def fast_modular_exponentiation(b, e, m):
    assert m > 0 and e >= 0
    if e == 0:
        return 1
    if e == 1:
        return b
    if e % 2 == 0:
        return fast_modular_exponentiation((b * b) % m, e // 2, m)
    else:
        return (fast_modular_exponentiation(b, e - 1, m) * b) % m


assert fast_modular_exponentiation(314159265358, 2718281828, 123456789) == 32073907