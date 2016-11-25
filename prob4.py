#!/usr/bin/python
# -*- coding:utf-8 -*-
xs=1
xm=60*xs
xh=60*xm
xd=24*xh
print "ingrese numero de dias"
d = float(raw_input())
print "ingrese numero de horas"
h = float(raw_input())
print "ingrese numero de minutos"
m = float(raw_input())
print "ingrese numero de segundos"
s = float(raw_input())

print (s*xs)+(m*xm)+(h*xh)+(d*xd),"segundos"

