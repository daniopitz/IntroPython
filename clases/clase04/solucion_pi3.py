#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 10:19:32 2022

@author: danielaudd
"""

k=0

suma=0

verificador=True

while verificador==True:
    sk=((-1)**k)/(2*k+1)
    suma=sk + suma
    if abs(sk) <=0.00001:
        verificador=False
    k=k+1  
print(suma*4)