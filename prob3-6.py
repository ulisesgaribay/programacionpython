#!/usr/bin/python
# -*- coding:utf-8 -*-
print "ingresa numero de años humanos"
x = float(raw_input())
def convierte(x):
	if 0 <= x <= 2:
		x = x*10.5
		return x
	if x > 2:
		x = (x-2)*4+2*10.5
		return x
x = convierte(x)
if x >= 0:
	print "el numero de años perro equivalente es: ",x,"años perro"
elif x < 0:
	print "ERROR!: no se admiten años negativos"
