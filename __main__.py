from math import ceil, sqrt

def isPrime(n):
  for i in range(2, ceil(sqrt(n))):
    if n % i == 0:
      return False
  return True

n = int(input("Enter a number: "))
if isPrime(n):
  print(f'{n} is prime')
else:
  print(f'{n} is not prime')
