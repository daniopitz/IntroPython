#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 13:58:40 2023

@author: daniela
"""

def escribir_tweets(texto, claves):
    lista_texto=texto.split()

    lista_aux=[]
    for e in lista_texto: #si detecto palabra clave agrego #
        if e in claves:
            lista_aux.append('#' + e)
        else:
            lista_aux.append(e)
         


    lista_aux2=[]

    for e in lista_aux: #corto las palabras y agrego @
        if len(e) > 4:
            palabra=e[:3] + '@'
            lista_aux2.append(palabra)
        else:
            lista_aux2.append(e)
  

    return ' '. join(lista_aux2)[0:154]

print('Solucion')

texto_input="No quiero ser alarmista pero mi padre tiene una empresa de alarmas y seguridad y la voy a heredar."

palabras_clave=['alarmas', 'seguridad']

print(escribir_tweets(texto_input, palabras_clave))
            