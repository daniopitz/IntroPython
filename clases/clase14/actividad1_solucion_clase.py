#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 14:52:33 2023

@author: daniela
"""



personas=['Juan', 'Maria', 'Pedro', 'Lucia']
edad=[23,13,4,5]

with open('archivo4.csv', 'w') as file:
    for i in range(len(personas)):
        linea=personas[i] +',' + str(edad[i]) + '\n'
        print(linea)
        file.write(linea)
    

