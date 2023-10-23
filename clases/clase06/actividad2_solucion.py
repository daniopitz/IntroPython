#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 11:08:41 2023

@author: daniela
"""

precios = [7875, 15562, 22500, 11437, 4492]
cantidades = [3, 2, 4, 1, 5]
productos = ["manzanas", "leche", "pan", "huevos", "agua"]

max_prec=max(precios)
min_prec=min(precios)

total=0

for i in range(len(precios)):
    total+=precios[i]*cantidades[i]
    
print('Valor total compra:', total, 'CLP')

print('Producto más caro:', productos[precios.index(max_prec)] + 'con un valor de',  precios[precios.index(max_prec)])
print('Producto más barato:', productos[precios.index(min_prec)] + 'con un valor de',  precios[precios.index(min_prec)])
