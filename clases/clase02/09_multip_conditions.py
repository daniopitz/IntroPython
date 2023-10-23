#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 10:20:15 2023

@author: calipsotornasol
"""

#codigo que pide confirmar una instalación por teclado
var = input('¿Desea instalar el programa seleccionado? [Y/N] ')
if (var =='Y' or var =='y'):
    print("Tu respondiste Sí")
elif(var =='N' or var =='n'):
    print("Tu respondiste No")
else:
    print("Input invalido")