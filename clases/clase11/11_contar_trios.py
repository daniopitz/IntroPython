#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 19:46:33 2023

@author: danielaudd
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



for i in range(7):
    carta=baraja.pop()
    cartas_jugador.append(carta)
    
for carta in cartas_jugador:
    print(carta)
    
print('Cartas Jugador')


numeros=[]

for carta in cartas_jugador:
    numeros.append(carta[0])

print(numeros)
#contar cuantas veces aparece un número en la mano

contador=0
CONTADORES=[0]*len(VALORES) # un contador por numero

   
for i in range(len(VALORES)):
    valor=VALORES[i]
    CONTADORES[i]=numeros.count(valor)
    
print('Contador', list(zip(VALORES, CONTADORES)))
    
#contar trios 

trios=0

for contador in CONTADORES:
    trio=contador//3
    trios+=trio

print(trios)
        

       

        
    

