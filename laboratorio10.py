# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 16:12:44 2020

@author: Henry Rueda
"""

potencia=0
a=int(input("ingrese a: "))
b=int(input("ingrese b: "))
suma=1
for i in range(b):
    potencia= a*suma
    suma=potencia

def a_power_b():
    print("el resultado de la potencia es: " + str(potencia))
    
a_power_b()