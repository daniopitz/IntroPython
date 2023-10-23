#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 16:00:12 2023

@author: daniela
"""
comunas=[]
contagiados=[]
with open('2020-05-01-CasosConfirmados.csv', 'r') as file:
    next(file)
    for line in file:
        if line.startswith('Metro')==True:
            lista_aux=line.split(',')
            comunas.append(lista_aux[2])
            contagiados.append(float(lista_aux[5]))
        
print(comunas)
print(contagiados)
    