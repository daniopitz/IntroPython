#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 10:36:17 2023

@author: daniela
"""

import random 

TRAJES = ['Picas', 'Diamantes', 'Treboles', 'Corazones']

VALORES = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
         'Jota', 'Reina', 'Rey', 'As']

baraja=[]

for i in range(len(TRAJES)):
    for j in range(len(VALORES)):
        baraja.append((VALORES[j],TRAJES[i]))
                

#barajar
random.shuffle(baraja)


#repartir
cartas_jugador=[]

for i in range(9):
    carta=baraja.pop()
    cartas_jugador.append(carta)
 
print('Cartas Jugador')

for carta in cartas_jugador:
    print(carta)
    
    
#contar trios

trios=dict()

for carta in cartas_jugador:
    if carta[0] in trios:
        trios[carta[0]]+=1
         
    else:
        trios[carta[0]]=1
 
print('Contador de cartas')

contador_trios=0

for llave, valor in trios.items():
    contador_trios+=valor//3
    
print('Numero de trios', contador_trios)
        
