
suma=0
k=0
sk=100 #un valor cualquiera que sea mayor a 10**(-5)
while abs(sk)>10**(-5):
    sk=(-1)**k/(2*k+1)
    suma+=sk
    k=k+1
print(4*suma)
