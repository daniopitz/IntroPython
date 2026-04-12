from math import sqrt
n=144
x0=n/2
a=True
while a==True:
    x=1/2*(x0+n/x0)
    if abs(x-x0)<=10**(-7):
        a=False
    x0=x
print(x)

    
    
