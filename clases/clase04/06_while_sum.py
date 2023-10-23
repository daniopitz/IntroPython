#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 16:28:02 2023

@author: danielaudd
"""
n=100
i=1
suma=0

while i <=n:
    print(i)
    fraccion=1/i
    suma=suma + fraccion
    i=i+1
    
print('La suma de 1/n desde 1 a', n, 'es:', suma)