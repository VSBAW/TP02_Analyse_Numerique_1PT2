# -*- coding: utf-8 -*-
"""Bonjour Madame/Monsieur, Voici notre progamme dédié a la resolution  par le théorème du point fixe des équations"""
"""Nous avons établi tout d'abord une fonction test dont nous avions calculé le resultats auparavant"""


from math import *
import numpy
def PointFixe (g, x0, epsilon, Nitermax) :
    n = 1
    xold = x0
    xnew = g(xold)
    difference = xnew-xold
       
    while abs(difference) > epsilon and n < Nitermax :
        xnew = g(xold)
        n= n+1
        difference = xnew - xold
        xold = xnew
        print (xnew, n, xnew - xold)
    return xnew

print ("="*5,"Fonction test","="*5)
import math
def gtest(x):
    return (1+ math.sin(x))/2
sol = PointFixe(gtest, 0, 1E-10, 1E4)

print ("La fonction test semble vrai donc le code semble aussi vrai")

print ("="*5,"Fonction 1","="*5)

def g1(x):
    return(9-3*x)**(1/4)

a = PointFixe (g1, -2, 1E-10, 1E4)
print(a, "Voila le resultat")

def g1bis(x):
    return -((9-3*x)**(1/4))

b = PointFixe (g1bis, 0, 1E-10, 1E4)
print(b, "Voila le résultat")

print ("="*5,"Fonction 2","="*5)

def g2(x):
    return (acos((x+2)/3))
c = PointFixe (g2, 0, 1E-10, 1E4)
print (c, "Voila le resultat")


def g2bis(x):
    return -(acos((x+2)/3))
cbis = PointFixe (g2bis, 0, 1E-10, 1E4)
print (cbis, "Voila le resultat")

print ("="*5,"Fonction 3","="*5)

def g3(x):
    return log(7/x)
d= PointFixe (g3, 1, 1E-10, 1E4)
print(d, "Voila le résultat")

print ("="*5,"Fonction 4","="*5)

def g4(x):
    return log(10+x)
e= PointFixe (g4, 0, 1E-10, 1E4)
print(e, "Voila le résultat")

print ("="*5,"Fonction 5","="*5)

def g5(x):
    return atan(((x+5)/2))
f= PointFixe (g5, 0, 1E-10, 1E4)
print(f, "voila le resultat")

print ("="*5,"Fonction 6","="*5)

def g6(x):
    return log((x**2)+3)
g= PointFixe (g6, 0, 1E-10, 1E4)
print (g, "Voila le résultat")

print ("="*5,"Fonction 7","="*5)

def g7(x):
    return (7-4*log(x))/3
h=PointFixe(g7,1,1E-10,1E4)
print(h, "Voila le resultat")

print ("="*5,"Fonction 8","="*5)

def g8(x):
    return ((2*(x**2)-(4*x)+17)**0.25)
i=PointFixe(g8,0,1E-10,1E4)
print(i, "Voila le résultat")

def g8bis(x):
    return -((2*(x**2)-(4*x)+17)**0.25)
j=PointFixe(g8bis,0,1E-10,1E4)
print (j, "Voila le résultat")

print ("="*5,"Fonction 9","="*5)

def g9(x):
    return log(2*sin(x)+7)
k = PointFixe(g9,0,1E-10,1E4)
print(k,"Voila le resultat")

print ("="*5,"Fonction 10","="*5)

def g10(x):
    return log(10)-log(log(x**2+4))
l = PointFixe(g10,0,1E-10,1E4)
print (l, "Voila le résultat")