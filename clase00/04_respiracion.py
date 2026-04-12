#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  3 22:24:04 2025

@author: daniela
"""

resp_min=12 #por minuto
resp_max=20 #por minuto

diff_tiempo_h=12

tiempo_m=diff_tiempo_h*60

print('Tiempo en minutos:',tiempo_m)
resp_min_actual=tiempo_m*resp_min
resp_max_actual=tiempo_m*resp_max

print('Minimo', resp_min_actual)
print('Maximo', resp_max_actual)
