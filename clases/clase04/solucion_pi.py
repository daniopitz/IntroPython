#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 10:04:00 2022

@author: danielaudd
"""

k=0
sk = 1
suma=0

while abs(sk) > 0.00001:
    sk=((-1)**k)/(2*k+1)
    print(k, sk)
    suma=sk + suma
    k=k+1  
    
print(suma*4)