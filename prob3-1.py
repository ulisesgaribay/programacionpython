#!/usr/bin/python
# -*- coding:utf-8 -*-
import math
print "latitud 1 en grados:"
t1 = float(raw_input())
print "longitud 1 en grados"
t2 = float(raw_input())
print "latitud 2 en grados"
g1 = float(raw_input())
print "longitud 2 en grados"
g2 = float(raw_input())
#conversiones
a = (t1*math.pi)/180
b = (t2*math.pi)/180
c = (g1*math.pi)/180
d = (g2*math.pi)/180

distancia = 6371.01*math.acos(math.sin(a)*math.sin(c)
	    +math.cos(a)*math.cos(c)*math.cos(b-d))
print "la distancia en km es: ", distancia
