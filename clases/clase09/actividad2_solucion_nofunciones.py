from math import sqrt

L = [3,3,3,3]

s = 0

for e in L:
    s += e
prom = s / len(L)

d = 0

for e in L:
    d += (e - prom)*(e - prom)
sd = sqrt(d / (len(L)-1))

print(sd)
