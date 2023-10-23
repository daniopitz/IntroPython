#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 17:07:21 2023

@author: daniela
"""
from random import randint

lista=[]

while True:
    n=randint(1,20)
    if n not in lista:
        lista.append(n)
    
    if len(lista)==7:
        break
    
loteria=lista[0:6]
print(loteria)

comodin=lista[6]
print(comodin)

carton=[]

posibles_numeros=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

validador1=False
validador2=False
while validador1==False and validador2==False:
    n= int(input('Ingrese numero para el cartón:'))
    if n in posibles_numeros:
        print('Numeros en el rango correcto')
        validador1=True
    if n not in carton:
        carton.append(n)
    if len(carton)==6:
        print('Carton lleno')
    else:
        print('Numeros en el rango incorrecto')
    
    
    