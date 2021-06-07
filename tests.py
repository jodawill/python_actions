from prime import *
from sys import exit

def test(f, expect, *args):
  if f(*args) == expect:
    print(f'TEST: {f.__name__}{args} -- PASS')
    return 0
  else:
    print(f'TEST: {f.__name__}{args} -- FAIL')
    return 1

exit_code = 0
exit_code |= test(isPrime, True, 17)
exit_code |= test(isPrime, False, 24)
exit_code |= test(isPrime, False, 1)
exit(exit_code)
