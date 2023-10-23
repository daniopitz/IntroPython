#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 12:12:40 2021

@author: danielaudd
"""

suma=0
k=0
sk=1

while abs(sk) > 0.00001:
    sk= ((-1)**k)/(2*k+1)
    suma= suma + sk
    k=k+1
    
print(4*suma)
    
    
