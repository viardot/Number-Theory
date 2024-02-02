# Least Common Multiple of two positive integers

def gcd(a, b):
  assert a >= 0 and b >= 0 and a + b > 0

  while a > 0 and b > 0:
    if a >= b:
      a = a % b
    else:
      b = b % a

  return max(a, b)

def lcm(a, b):
  assert a > 0 and b > 0
  
  d = gcd(a, b)

  return int((a * b) / d)

assert lcm(2, 3) == 3
assert lcm(10, 15)  == 60
assert lcm(35, 70) == 70