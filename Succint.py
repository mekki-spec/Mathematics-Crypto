def g(a, b):
  return (0.5 * a - 1 / 3 * b * b, a)
def h(n):
  a, b = 1.0, 2.0
for j in range(n):
  a, b = g(a, b)
return a, b
def approx(prec):
  a, b = 1.0, 2.0
n = 0
while abs(b) > prec: #attention aux négatifs
a, b = g(a, b)
n = n + 1
return n