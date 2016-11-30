#!/usr/bin/python
# -*- coding:utf-8 -*-
print "ingresa tu nombre la primer letra en mayusculas: "
x = [raw_input()]
y = x[0][0]
vo = "la primer letra %s de tu nombre es vocal "%y
def evalua(y):
	if y == "A":
		print vo
	elif y == "E":
		print vo
	elif y == "O":
		print vo
	elif y == "O":
		print vo
	elif y == "U":
		print vo
		return y
	else:
		print "la primer letra %s de tu nombre es consonante "%y
y = evalua(y)
