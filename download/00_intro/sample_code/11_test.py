def mult_and_abs(x, y):
    z = x * y
    if z >= 0:
        return z
    else:
        return z * -1

def test_mult_and_abs():
  assert(mult_and_abs(-3,2) == 6), "Error"
  return "Test passed!"

print(test_mult_and_abs())