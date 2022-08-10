# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 17:54:23 2022

@author: Nico
"""
#We define several vectors.


def vectores(dimension, number_of_vectors):
    vectores = []
    for m in range(number_of_vectors):
        vector_a = [f'a{i}{m}' for i in range(dimension)]
        vector_b = [f'b{i}{m}' for i in range(dimension)]
        vector_a.extend(vector_b)
        vectores.append(vector_a)
    return vectores

#For our final formula is a good idea extract from vectores his variables.
    
def variables(dim, numb, m):
    resp0 = []
    for i in range(numb):
        a = vectores(dim,numb)[i]
        resp0.extend(a)
    return resp0[:m]

#Cause a structure from inner dot in complex numbers we define
#several functions for useness.

def transponer(vect):
    a = int(len(vect)/2)
    v1 = vect[a:]
    v2 = vect[:a]
    v1.extend(v2)
    return v1

def prod_uno(vect1,vect2):
    resp = []
    for i in range(len(vect1)):
        a = vect1[i]+'*'+vect2[i]
        resp.append(a)
    
    return '+'.join(resp)

def prod_dos(vect1,vect2, dim):
    resp2 = []
    for i in range(len(vect1)):
        if i<dim:
            a = vect1[i]+'*'+transponer(vect2)[i]
            resp2.append(a)
        else:
            a = '(-'+vect1[i]+')*'+transponer(vect2)[i]
            resp2.append(a)
    return '+'.join(resp2)

#Firstly we construct cuadratics equations. No matter recent definitions.

def cuadratic_p(vect1,m, dim):
    listando = []
    a = int(len(vect1)/2)
    for i in range(a):
        b= vect1[i]+'^2+'+vect1[a+i]+f'^2==1/{dim}'
        listando.append(b)
    return '&&'.join(listando[:m])

#Finally we construct ours cuartic equations.

def cuartics(dim, numb,l):
    listado = []
    for i in range(numb):
        if i>0:
            for j in range(i):
                equation_1 ='('+prod_uno(vectores(dim, numb)[i],vectores(dim, numb)[j])+')^2'
                equation_2 = '('+prod_dos(vectores(dim, numb)[i],vectores(dim, numb)[j], dim)+')^2'
                equation_3 = equation_1+'+'+equation_2+f'==1/{dim}'
                listado.append(equation_3)
        else:
            continue
    return '&&'.join(listado[:l])

#And make us capable for calculate the formulae to send to Mathematica. We
#introduce the dimension (dim) and the number of vectors (n), the output 
#contains equations for n vectors mutually unbiased; l quartics, s cuadratics.
#The existential formulae search about r variables. 

def build_formula(dim, numb, l, s, r):
    a = cuartics(dim,numb,l)
    resp3 = []
    for i in range(numb):
        b = cuadratic_p(vectores(dim,numb)[i], s, dim)
        resp3.append(b)
    
    ex_vari = 'Exists[{'+','.join(variables(dim,numb,r))+'},'
    formula = ex_vari+'&&'.join(resp3)+'&&'+a+']'
    return formula

#Gives an example for revision.
formula_posta = build_formula(2,3,3,6,7)
    
               