#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 22:33:06 2023

@author: danielaudd
"""

sk=1
k=0
suma=0

while abs(sk) > 0.00005:
    sk=(-1)**k/(2*k+1)
    suma=suma+sk
    k=k+1
   
print(4*suma, 'k:', k-1)


k=0
suma=0

while True:
    sk=(-1)**k/(2*k+1)
    suma=suma+sk
    if abs(sk) <= 0.00005:
        print(4*suma,'k:', k)
        break
    k=k+1
    

a=True
k=0
suma=0

while a==True:
    sk=(-1)**k/(2*k+1)
    suma=suma+sk
    if abs(sk) <= 0.00005:
        a=False
        print(4*suma, 'k:',k)
    k=k+1
    

    
    