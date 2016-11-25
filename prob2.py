#!/usr/bin/python
# -*- coding:utf-8 -*-
print "ingresa tu salario"
x = float(raw_input())
print "el interes generado es: "
i = x*0.04
print i
def interas (y):
	sum=0
	for a in range(1,y+1):
		sum=sum+a
	return sum
print "ingresa el numero de años"
y = input()
print "tu salario en %d años es: "%y
print (y*x)+i+interas(y)
