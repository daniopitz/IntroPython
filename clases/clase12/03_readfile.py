#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 11:28:44 2022

@author: danielaudd
"""
comunas=[]
contagiados=[]
with open('2020-05-01-CasosConfirmados.csv', 'r') as file:
    next(file)
    for line in file:
        if line.startswith('Metropolitana')==True:
            print(line)
            lista_aux=line.split(',')
            comunas.append(lista_aux[2])
            contagiados.append(float(lista_aux[5]))
        
print(contagiados)
print(comunas)