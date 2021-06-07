from math_tools import *
from sys import exit

def test(f, expect, *args):
  if f(*args) == expect:
    print(f'TEST: {f.__name__}{args} -- PASS')
    return 0
  else:
    print(f'TEST: {f.__name__}{args} -- FAIL')
    return 1

exit_code = 0

# isPrime
exit_code |= test(isPrime, True, 17)
exit_code |= test(isPrime, False, 24)
exit_code |= test(isPrime, False, 1)

# isComposite
exit_code |= test(isComposite, False, 17)
exit_code |= test(isComposite, True, 24)
exit_code |= test(isComposite, False, 1)

# getFibonacci
exit_code |= test(getFibonacci, 0, 0)
exit_code |= test(getFibonacci, 1, 1)
exit_code |= test(getFibonacci, 1, 2)
exit_code |= test(getFibonacci, 2, 3)
exit_code |= test(getFibonacci, 3, 4)
exit_code |= test(getFibonacci, 5, 5)
exit_code |= test(getFibonacci, 8, 6)
exit_code |= test(getFibonacci, 13, 7)
exit_code |= test(getFibonacci, 21, 8)
exit_code |= test(getFibonacci, 34, 9)
exit_code |= test(getFibonacci, 55, 10)
exit_code |= test(getFibonacci, 89, 11)
exit_code |= test(getFibonacci, 6765, 20)

exit(exit_code)
