#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 12:17:22 2020

@author: danielaudd
"""

f = open("2020-05-01-CasosConfirmados.csv","r")
contagiados=list()
comunas=list()
for linea in f:
    lista=linea.split(',')
    if lista[0]=='Metropolitana':
        contagiados.append(float(lista[5]))
        comunas.append(lista[2])
f.close()



contagiados_sort=contagiados.copy() 
contagiados_sort.sort(reverse=True) 

min_contagiados=min(contagiados_sort[:5])


print('Solucion 1:')
print('Las comunas con mas contagiados son:' + '\n')
for i in range(len(contagiados)):
    if contagiados[i]>=min_contagiados:
        print(comunas[i], contagiados[i])
        
print('\n')

print('Solucion 2')

index_aux = 5*[0] #Creo una lista para guardar los indices

contagios_top5=contagiados_sort[:5]

print(contagios_top5)

for i in range (5):
    index_aux[i]=contagiados.index(contagios_top5[i])
    

print('Las comunas con más contagiados son:' + '\n')
for i in range(5):
    print(comunas[index_aux[i]], contagiados[index_aux[i]])
    
    
    
print('Solucion 3')        
import operator
contagios=[]

with open("2020-05-01-CasosConfirmados.csv","r") as f:
    next(f)
    for line in f:
        if line.startswith('Metropolitana'):
            lista_line=line.split(',')
            contagios.append((lista_line[2], float(lista_line[5])))
         
a=sorted(contagios, reverse=True, key=operator.itemgetter(1))


print(a[:5])
