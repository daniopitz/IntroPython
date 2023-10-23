#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 14:54:05 2023

@author: daniela
"""

from math import sqrt

def promedio(L):
    return sum(L)/len(L)

def desviacion(L):
    p=promedio(L)
    
    suma=0
    for e in L:
        suma+=(e-p)**2
    return sqrt(suma/(len(L)-1))

L=[70, 71, 71]

print(desviacion(L))
        