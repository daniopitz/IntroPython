#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 12:25:03 2021

@author: danielaudd
"""


nombreArchivo = input('Ingrese el nombre del archivo (incluyendo extension): ')

for i in range(len(nombreArchivo)):
    if nombreArchivo[i] == '.':
        nombre = nombreArchivo[0:i]
        extension = nombreArchivo[i+1:]
        break

print('El nombre del archivo es:', nombre)
print('La extension del archivo es:', extension)