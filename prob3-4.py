#!/usr/bin/python
# -*- coding:utf-8 -*-
print "ingresa un numero"
x = int(raw_input())
def identifica(x):
	if x%2 == 1:
		print "x es impar"
	elif x%2 == 0:
		print "x es par"
x = identifica(x)
