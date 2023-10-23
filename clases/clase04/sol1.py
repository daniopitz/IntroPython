#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 22:27:07 2023

@author: danielaudd
"""
from math import sin, pi
suma=0
for x in range(1,1001):
    y=100*sin(pi*x/1000)
    area=1*y
    suma=suma+area
    
print('El área es:', suma)
    
