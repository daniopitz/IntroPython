#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 22:05:04 2021

@author: danielaudd
"""

# esta linea import sin y pi desde la biblioteca math
from math import sin, pi
area = 0

for i in range(1000):
    y = 100 * sin(pi * i / 1000)
    area = area + y
print(area)