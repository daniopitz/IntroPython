def real_imag_conj(val):
    return val.real, val.imag, val.conjugate()

r,i,c = real_imag_conj(3 + 7j)

print(r)
print(i)
print(c)

