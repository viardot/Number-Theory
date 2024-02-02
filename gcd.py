# Greatest Common Devisor
# Euclid's algorithm, efficient implementation

def gcd(a, b):
  assert a >= 0 and b >= 0 and a + b > 0

  while a > 0 and b > 0:
    if a >= b:
      a = a % b
    else:
      b = b % a

  return max(a, b)

assert gcd(24, 16) == 8
assert gcd(790933790547, 1849639579327) == 3416723
assert gcd(790933790548, 2) == 2