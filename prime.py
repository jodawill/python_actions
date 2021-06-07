from math import ceil, sqrt

def isPrime(n):
  n == 1 and return False
  for i in range(2, ceil(sqrt(n))):
    if n % i == 0:
      return False
  return True
