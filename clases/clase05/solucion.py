#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 12:30:11 2021

@author: danielaudd
"""

condicion1=True
condicion2=True

while condicion1==True:
    ancho=int(input('ancho'))
    alto=int(input('alto'))
    if ancho < 30 and alto < 40: 
        condicion1=False

while condicion2==True:
    caracter=input('caracter (-, *, #)')
    if caracter == '-' or caracter=='*' or caracter=='#':
        condicion2=False
        

linea=caracter+' '*(ancho-2)+caracter

print(caracter*ancho)

for i in range (alto-2):
    print(linea)
print(caracter*ancho)