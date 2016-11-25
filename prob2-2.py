#!/usr/bin/python
# -*- coding:utf-8 -*-
tarifa= 8.74
print "ingrese numero de kilometros"
kmr = float(raw_input())
m = 1000.0*kmr
pormts = (m/250.0)*1.84
def coste(tarifa,pormts):
	coste = tarifa+pormts
	return coste
print "tu costo de uso de taxi fue: "
print coste(tarifa,pormts), "pesos"
