# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 19:14:48 2020

@author: Hi
"""

# preinforme11_HenryRueda

import numpy as np

# sacado de: rtve noticias 

covid_19= np.array([
    ['Estados Unidos','653825','33000','57271'],
    ['España','182816','22170','517'],
    ['Italia','168941','1809','2335'],
    ['Francia','141900','17941','30955'],
    ['Alemania','135843','4052','64300'],
    ['Reino unido','104135','13759','1918'],
    ['China','83403','3342','67017'],
    ['Iran','77995','4869','4590'],
    ['Turquia','74193','168','162'],
    ['Colombia','3233','144','550']])
    
# paises con mayor nummero de contagios y sus cifras
    
def pais_con_mayor_numero_de_contagios(covid_19):
    niveles,columnas=covid_19.shape
    mayor= covid_19[0,1]
    pais_mayor_covid_19= covid_19[0,0]
    for i in range(1,niveles):
        if int(mayor)< int(covid_19[i,1]):
            mayor= covid_19[i,1]
            pais_mayor_covid_19= covid_19[i,0]
    print("el pais con mas casos de covid_19 es: "+pais_mayor_covid_19 + " y tiene " + str(mayor) + " casos confirmados")
                        
pais_con_mayor_numero_de_contagios(covid_19)   

# pais con mayor numero de muertos y sus cifras

def pais_con_mayor_numero_de_muertos(covid_19):
    niveles,columnas=covid_19.shape
    mayor= covid_19[0,2]
    pais_mayor_covid_19= covid_19[0,0]
    for i in range(1,niveles):
        if int(mayor)< int(covid_19[i,2]):
            mayor= covid_19[i,2]
            pais_mayor_covid_19= covid_19[i,0]
    print("el pais con mas fallecidos de covid_19 es: "+pais_mayor_covid_19 + " y tiene " + str(mayor) + " fallecidos")
                        
pais_con_mayor_numero_de_muertos(covid_19)    

# pais con mayyor numero de recuperado y sus cifras

def pais_con_mayor_numero_de_recuperados(covid_19):
    niveles,columnas=covid_19.shape
    mayor= covid_19[0,3]
    pais_mayor_covid_19= covid_19[0,0]
    for i in range(1,niveles):
        if int(mayor)< int(covid_19[i,3]):
            mayor= covid_19[i,3]
            pais_mayor_covid_19= covid_19[i,0]
    print("el pais con mayor recuperacion de pacientes del covid_19 es: "+pais_mayor_covid_19 + " y tiene " + str(mayor) + " pacientes recuperados")
                        
pais_con_mayor_numero_de_recuperados(covid_19)    








