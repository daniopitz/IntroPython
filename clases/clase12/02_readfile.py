#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 10:59:06 2021

@author: danielaudd
"""

file = open('2020-05-01-CasosConfirmados.csv', 'r') #Abre el archivo
for line in file:
    print (line)
file.close() # Cierra el archivo

with open('2020-05-01-CasosConfirmados.csv', 'r') as file: #Abre el archivo
    for line in file:
        print(line)
