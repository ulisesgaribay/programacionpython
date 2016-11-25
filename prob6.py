#!/usr/bin/python
# -*- coding:utf-8 -*-
print "ingresa tu peso en kg"
P = float(raw_input())
print "ingresa tu altura en m"
A = float(raw_input())
def IMC(P,A):
	IMC = P/A**2
	return IMC
print "tu IMC entre tus kg y tu altura en m es: "
print IMC(P,A)
print "por lo tanto usted tiene: "
if IMC(P,A) < 16.0:
	print "Delgadez severa"
if 17.0 > IMC(P,A) >= 16.0:
	print "Delgadez moderada"
if 18.5 > IMC(P,A) >= 17.0:
	print "Delgadez leve"
if 25.0 > IMC(P,A) >= 18.5:
	print "Lo normal"
if 30.0 > IMC(P,A) >= 25.0:
	print "Sobrepeso"
if 40.0 > IMC(P,A) >= 30.0:
	print "Obesidad"
if IMC(P,A) >= 40.0:
	print "Obesidad morbida"

