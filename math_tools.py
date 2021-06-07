from math import ceil, sqrt

def isPrime(n):
  if n == 1:
    return False
  for i in range(2, ceil(sqrt(n))):
    if n % i == 0:
      return False
  return True

def isComposite(n):
  if n == 1:
    return False
  return not isPrime(n)

def getFibonacci(i):
  f, f_1, f_2, n = 0, 0, 1, 1
  while n < i + 1:
    f = f_1 + f_2
    n += 1
    f_2 = f_1
    f_1 = f
  return f
