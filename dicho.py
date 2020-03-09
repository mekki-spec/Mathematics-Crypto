def f(x):
  return x * x - 10
def dicho(a, b, n):
  for i in range(n):
  c = (a + b) / 2
if f(a) * f(c) <= 0:
  b = c
else :
  a = c
return a, b
def dichobis(a, b, prec):
  while b - a > prec:
  c = (a + b) / 2
if f(a) * f(c) <= 0:
  b = c
else :
  a = c
return a, b
def dichotomie(a, b, prec):
  if b - a <= prec:
  return a, b
else :
  c = (a + b) / 2
if f(a) * f(c) <= 0:
  return dichotomie(a, c, prec)
else :
  return dichotomie(c, b, prec)