#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 14:05:31 2023

@author: daniela
"""

personas = [("Juan", 30), ("María", 25), ("Pedro", 40), ("Lucía", 35)]

with open ('personas2.txt', 'w') as f:
    for persona in personas:
       linea=persona[0] + ',' + str(persona[1])
       f.write(linea+'\n')