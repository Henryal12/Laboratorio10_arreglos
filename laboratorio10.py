# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 16:12:44 2020

@author: Henry Rueda
"""

potencia=0
a=int(input("ingrese a: "))
b=int(input("ingrese b: "))
suma=1
if a!=0:
    if b!=0:
        for i in range(b):
            potencia= a*suma
            suma=potencia
    else:
        b=1
        for i in range(b):
            potencia= a/a
else:
    potencia=0
def a_power_b():
    if a!=0:
        print("el resultado de la potencia es: " + str(int(potencia)))
    else:
        print("el programa se ha detenido")
    
a_power_b()