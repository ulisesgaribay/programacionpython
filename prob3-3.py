#!/usr/bin/python
# -*- coding:utf-8 -*-
print "ingresa tu primer numero"
x = int(raw_input())
print "ingresa tu segundo numero"
y = int(raw_input())
print "ingresa tu tercer numero"
z = int(raw_input())
print "tus numeros ordenados de menor a mayor son: "
if x >= y >= z:
	print z,y,x
elif x >= z >= y:
	print y,z,x
elif y >= x >= z:
	print z,x,y
elif y >= z >= x:
	print x,z,y
elif z >= x >= y:
	print y,x,z
elif z >= y >= x:
	print x,y,z
