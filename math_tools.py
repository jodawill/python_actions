from math import ceil, sqrt

def isPrime(n):
  if n == 1:
    return False
  for i in range(2, ceil(sqrt(n))):
    if n % i == 0:
      return False
  return True

def isComposite(n):
  return not isPrime(n)
