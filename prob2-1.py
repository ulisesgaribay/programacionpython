#!/usr/bin/python
# -*- coding:utf-8 -*-
import math
print "ingresa el cateto adyacente: "
a = float(raw_input())
print "ingresa el cateto opuesto: "
b = float(raw_input())
def hipotenusa(a,b):
	hipotenusa = math.sqrt(a)+math.sqrt(b)
	return hipotenusa
print "tu hipotenusa es: "
print hipotenusa(a,b)

