#!/usr/bin/python
# -*- coding:utf-8 -*-
print "ingresa un numero"
n = int(raw_input())
print "tu lista es: "
print range(1,n+1)
print "la suma de tu lista es: "
def sumas(n):
	suma=0
	for sumar in range(1,n+1):
		suma=suma+sumar
	return suma
print sumas(n)
