#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 24 09:34:22 2021

@author: danielaudd
"""

def participacion_pais(file):
    votos=list()
    votantes=list()
    with open(file, "r") as f:
        next(f)
        for line in f:
            s=line.split(';')
            votos.append(int(s[11]))
            votantes.append(int(s[10]))
            return round((sum(votos)/sum(votantes))*100,2)

print(participacion_pais('resultados_comuna.csv'))