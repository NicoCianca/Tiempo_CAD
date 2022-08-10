# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 19:46:14 2022

@author: Nico
"""
import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.optimize import curve_fit
from formulea import build_formula
from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl, wlexpr
session = WolframLanguageSession()
pyresolve = session.function(wl.Resolve)

tiempo=[]
for i in range(12):
    for j in range(18):
        formula = build_formula(24, 2, 36, 2*(j+1), 18-i)
        t1=time.time_ns()
        resultado = pyresolve(wlexpr(formula))
        t2=time.time_ns()
        print(resultado)
        delta=t2-t1
        tiempo.append(delta)

tiempon = np.array(tiempo[0:])

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
plt.xlabel('quiting equations')
plt.ylabel('tiempo(ns)')
#plt.plot(variab, modelo(variab, *popt),'r-')
#plt.plot(variab, modelo_alt(variab, *popt2), 'g-')

#print(popt,pcov)
#print(popt2,pcov2)