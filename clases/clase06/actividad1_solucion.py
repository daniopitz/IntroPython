#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 10:57:48 2022

@author: danielaudd
"""
from math import sqrt

tiempos = [67, 45, 84]

prom= sum(tiempos)/len(tiempos)

print('Promedio', round(prom,3))

suma=0
for tiempo in tiempos:
    print(tiempo)
    suma = suma + (tiempo - prom)**2
    
stdev= suma
    
print(round(sqrt(suma/(len(tiempos)-1)),3))
    
    



