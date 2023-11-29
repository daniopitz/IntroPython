#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 22:59:37 2020

@author: danielaudd
"""

regiones=list()
casos=list()
with open("2020-06-01-CasosConfirmados-totalRegional.csv", "r") as t:
    next(t)
    for line in t:
        s=line.split(',')
        region=s[0]
        numero=s[2]
        print(region, numero)
        if region == 'Total':
            continue
        regiones.append(region)
        casos.append(int(s[2]))
  
print(regiones)
print(casos)
    
pcr=list()

with open("pcr.csv", "r") as g:
    next(g)
    for line in g:
        s=line.split(',')
        pcr.append(int(s[-1]))#la ultima columna
        
print(pcr)

  
#escribimos el archivo  
f = open("positividad.csv", "w")
positividad=list()
header=['Region','PCRs','Casos','Positividad']
f.write(','.join(header)+'\n')
for i in range(len(pcr)):
    if pcr[i]>0:
        positividad.append(casos[i]/pcr[i]*100)
    else:
        positividad.append(0)
    linea=[regiones[i],str(pcr[i]),str(casos[i]),str(round(positividad[i],2))]
    f.write(','.join(linea)+'\n')
f.close()