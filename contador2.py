# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 19:46:14 2022

@author: Nico
"""
import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.optimize import curve_fit
from formulador import build_formula
from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl, wlexpr
session = WolframLanguageSession()
pyresolve = session.function(wl.Resolve)

tiempo=[]
for i in range(8):
    formula = build_formula(2, 2, 1, 1, i+1)
    t1=time.time_ns()
    resultado = pyresolve(wlexpr(formula))
    t2=time.time_ns()
    print(resultado)
    delta=t2-t1
    tiempo.append(delta)

tiempon = np.array(tiempo[1:])

def modelo(x,a,b):
    return a*np.exp(b*x)

def modelo_alt(x,a,b,c):
    return a*np.exp(b*np.exp(c*x))

parametros_inicio_alt = [1.4e10, -8.08, -0.03]
parametros_inicio = [2.6e08,0.1]
variab = np.linspace(0,i+1,i)

#popt, pcov = curve_fit(modelo, variab, tiempon, p0=parametros_inicio)
#popt2, pcov2 = curve_fit(modelo_alt, variab, tiempon, p0=parametros_inicio_alt)

plt.figure()
plt.plot(tiempon,'*')
plt.xlabel('reduced_variables')
plt.ylabel('tiempo(ns)')
#plt.plot(variab, modelo(variab, *popt),'r-', label='18cuadratic+1cuartic')
#plt.plot(variab, modelo_alt(variab, *popt2), 'g-')

#print(popt,pcov)
#print(popt2,pcov2)