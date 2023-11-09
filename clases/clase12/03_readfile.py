#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 11:28:44 2022

@author: danielaudd
"""
comunas=[]
contagiados=[]
with open('2020-05-01-CasosConfirmados.csv', 'r') as file:
    next(file) #me salto la fila 1
    for line in file:
        if line.startswith('Metropolitana')==True:
            lista_aux=line.split(',')
            comunas.append(lista_aux[2])
            contagiados.append(float(lista_aux[5]))
        
contagiados_back=contagiados.copy() #comentario
contagiados.sort(reverse=True)
contagiados_top5=contagiados[0:5]
minimo=min(contagiados_top5)


for k in contagiados_back:
    if k >=minimo:
        comuna=comunas[contagiados_back.index(k)]
        print(comuna,k)
        
        

