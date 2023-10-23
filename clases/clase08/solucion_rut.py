#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 15:03:10 2023

@author: danielaudd
"""
rut=input('Ingrese su rut con guión y dígito verificador:')
suma=0
    
n = [3,2,7,6,5,4,3,2] #asumimos que el rut tiene 8 dígitos

rut_base=rut[:-2] #elimino el guion y el digito verificado
    
d_verificador=rut[-1] #dígito verificador
    
rut_list=[]
    
        
    
for i in range(len(rut_base)):
    suma=suma+int(rut_base[i])*n[i]
        
resto=suma%11
    
d=11-resto
    
if d == 10 and (d_verificador=="k" or d_verificador=="K"):
    print(True)
elif d==11 and d_verificador=='0':
    print(True)
elif d==int(d_verificador):
    print(True)
else:
    print(False)

