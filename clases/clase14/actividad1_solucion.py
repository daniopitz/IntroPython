#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 10:48:29 2023

@author: calipsotornasol
"""

personas=['Juan', 'Maria', 'Pedro', 'Lucia']
edad=[23, 13,4,5]

with open('personas1.txt', 'w') as file:
    for i in range(len(personas)):
        file.write(personas[i] + ' ' + str(edad[i]) + '\n')
        
    




