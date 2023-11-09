#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 18:12:58 2021

@author: danielaudd
"""

texto= "No quiero ser alarmista pero mi padre tiene una empresa de alarmas y seguridad y la voy a heredar."

claves=['alarmas', 'seguridad']

lista=texto.split() #paso el texto a lista

lista_aux=list()

for e in lista: #si detecto palabra clave agrego #
    if e in claves:
        lista_aux.append('#' + e)
    else:
        lista_aux.append(e)
        



lista_aux2=list()

for e in lista_aux: #corto las palabras y agrego @
    if len(e) > 4:
        palabra=e[:3] + '@'
        lista_aux2.append(palabra)
    else:
        lista_aux2.append(e)
print(lista_aux2)

print(' '. join(lista_aux2)[0:154])
    