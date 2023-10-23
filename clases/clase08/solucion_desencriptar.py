#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 12:16:11 2020

@author: danielaudd
"""


palabra = input('Ingrese palabra a desencriptar: ')
clave = 'murcielago'
salida1=[]

for e in palabra:
    if e.isdigit() == True:
        a = clave[int(e)]
        salida1.append(str(a))
    else:
        salida1.append(e)

palabra_desencriptada1 = ''.join(salida1)
print('Palabra encriptada', palabra_desencriptada1)



