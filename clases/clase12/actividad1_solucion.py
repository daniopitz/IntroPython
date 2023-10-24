#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 08:38:47 2023

@author: calipsotornasol
"""

pobreza_reg={'Tarapaca' : 7.1, 'Antofagasta' : 5.4, 'Atacama' : 6.9, 'Coquimbo' :
13.8, 'Valparaíso' : 12.0, 'Libertador Bernardo OHiggins' : 13.7, 'Maule' : 18.7,
'Biobío' : 17.6, 'La Araucanía' : 23.6, 'Los Lagos' : 16.1, 'Aysen' : 6.5,
'Magallanes y La Antártica Chilena' : 4.4, 'Región Metropolitana de Santiago' : 7.1,
'Los Ríos' : 16.8, 'Arica y Parinacota' : 9.7}
    
pobreza=list(pobreza_reg.values())

maximo=max(pobreza)


for region, per in pobreza_reg.items():
    if per==maximo:
        print(region, per)