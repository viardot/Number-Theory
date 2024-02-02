def ext_gcd(m, n):
  assert m >= n and n >= 0 and m + n > 0
  if n == 0:
    d, x, y = m, 1, 0
  else:
    (d, p, q) = ext_gcd(n, m % n)
    x = q
    y= p - q * (m // n)

  assert m % d == 0 and n % d == 0
  assert d == m * x + n * y

  return (d, x, y)  


def gcd(a, b):
  assert a >= 0 and b >= 0 and a + b > 0

  while a > 0 and b > 0:
    if a >= b:
      a = a % b
    else:
      b = b % a
  return max(a, b)

def diophantine(a, b, c):
  

  if a > b:
    q = ext_gcd(a, b)
    x1 = q[1]
    y1 = q[2]
  else:
    q = ext_gcd(b, a)
    x1 = q[2]
    y1 = q[1]  

  assert c % q[0] == 0
  d = q[0]
  p = c / d

  return (int(p*x1), int(p*y1))

assert diophantine(24, 16, 64) == (8, -8)