# FastModularExponentiation(b, k ,m) that computes (b * b)^k mod m
# using only around 2k modular multipliction.

def FastModularExponentiation(b, k, m):
  b %= m

  for _ in range (k):
    b = b ** 2 % m

  return b