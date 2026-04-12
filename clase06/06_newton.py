from math import sqrt
n = 144
x = n / 2
x0 = x + 1
while abs(x - x0) > 10**(-7):
    x0 = x
    x = 1/2 * (x0 + n/x0)
print(x)

