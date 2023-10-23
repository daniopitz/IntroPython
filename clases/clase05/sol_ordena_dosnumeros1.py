#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 22:55:16 2023

@author: danielaudd
"""

a=input('Ingresa un numero a:')
b=input('Ingresa un numero b:')

if b<a:
   t=a
   a=b
   b=t
    
print(a)
print(b)
