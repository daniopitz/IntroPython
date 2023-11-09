#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 23 17:28:13 2021

@author: danielaudd
"""
import operator

def participacion_comuna(file):
    participacion=list()
    with open(file, "r") as f:
        next(f)
        for line in f:
            s=line.split(';')
            p=int(s[11])/int(s[10])*100
            participacion.append((s[0],p))
            a=sorted(participacion, reverse=True, key=operator.itemgetter(1))
    return a[:10]

print(participacion_comuna('resultados_comuna.csv'))