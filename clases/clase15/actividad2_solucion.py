#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 23 17:33:00 2021

@author: danielaudd
"""

def resultados_comuna_rm(file):
    with open(file, "r") as f:
        with open("resultados_comuna_rm.csv", 'w') as g:
            for line in f:
                s=line.split(';')
                if s[0]=='Comuna'.strip():
                    header=s.copy()
                    header_new= [e.replace('\n', '') for e in header]
                    header_new.append('Participacion')
                    #print(header_new)
                    g.write(';'.join(header_new) + '\n')
                elif s[1].startswith('13')==True:
                    p=str(round(int(s[-1])/int(s[-2])*100,2))
                    lines_rm=s.copy()
                    lines_rm.append(p)
                    lines_rm_new = [e.replace('\n', '') for e in lines_rm]
                    g.write(';'.join(lines_rm_new) + '\n') 
                    
resultados_comuna_rm('resultados_comuna.csv')                   