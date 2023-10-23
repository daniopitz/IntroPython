#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 22:05:56 2021

@author: danielaudd
"""

for i in range(1, 3001):
    j = str(i)
    jr = j[::-1]
    if j == jr:
        print(i)

