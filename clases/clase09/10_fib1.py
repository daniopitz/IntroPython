def fibonacci(N, a=0, b=1):
    L = []
    while len(L) < N:
        c = a
        a = b
        b = c + b
        L.append(a)
    return L
    
print(fibonacci(10,a=1, b=2))

