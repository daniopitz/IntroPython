#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 09:23:24 2023

@author: danielaudd
"""

import random

# Definir una baraja de cartas francesas
def crear_baraja():
    baraja = []
    palos = ['Corazones', 'Diamantes', 'Picas', 'Tréboles']
    valores = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    for palo in palos:
        for valor in valores:
            baraja.append(valor + ' de ' + palo)
    return baraja

# Mezclar la baraja de cartas
def mezclar_baraja(baraja):
    random.shuffle(baraja)
    return baraja

# Repartir cartas a los jugadores
def repartir_cartas(baraja, num_jugadores, cartas_por_jugador):
    manos = []
    for i in range(num_jugadores):
        mano = []
        for j in range(cartas_por_jugador):
            carta = baraja.pop()
            mano.append(carta)
        manos.append(mano)
    return manos

print('Manos')
# Ejecutar el juego
baraja = crear_baraja()
baraja = mezclar_baraja(baraja)
manos = repartir_cartas(baraja, 4, 5)
for mano in manos:
    print(mano)
