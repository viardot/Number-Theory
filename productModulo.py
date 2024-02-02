# Compute the remainder modulo m of the product of a sequence of integers.

def product_modulo(lst, modulo):
    product = 1
    for element in lst:
        product = (product * element) % modulo

    return product

assert product_modulo([3, 7], 2) == 1
assert product_modulo([3, 11], 10) == 3
assert product_modulo([6, 4], 5) == 4