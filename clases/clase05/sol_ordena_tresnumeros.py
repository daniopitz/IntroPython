#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 23:05:21 2023

@author: danielaudd
"""

a=input('Ingresa un numero a:')
b=input('Ingresa un numero b:')
c=input('Ingresa un numero c:')


if b<a:
   a,b=b,a

   
if c<a:
   a,c=c,a
  
    
if c<b:
   c,b=b,c



    
print(a)
print(b)
print(c)
