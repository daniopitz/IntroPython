#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 10:28:29 2021

@author: danielaudd
"""

# 1- verifica si es un digito

s1='H'

print(s1.isdigit())


# 2- retorna el indice del caracter

s2='Hola'
print(s2.index('o'))

# 3- agrega un elemento a la lista

L=['1', 'Hola', 'Olivia']
L.append('Gata')

print(L)

# 4- convierte una lista a string

L2=['1', '2', '3']
print('-'.join(L2))