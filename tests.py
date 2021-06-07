from prime import *

def test(f, expect, *args):
  if f(*args) == expect:
    print(f'TEST: {f.__name__}{args} -- PASS')
  else:
    print(f'TEST: {f.__name__}{args} -- FAIL')

test(isPrime, True, 17)
test(isPrime, False, 24)
test(isPrime, False, 1)
