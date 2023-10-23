#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 10:52:34 2023

@author: calipsotornasol
"""

suma=0
sk=1
k=0

while abs(sk) > 0.00001:
    sk=(-1)**k/(2*k+1)
    suma=suma+sk
    k=k+1
    
print('Resultado',4*suma)