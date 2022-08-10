# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 20:43:01 2022

@author: Nico
"""

#We define a function to create the formulaes to n variables


#What a shame my method to construct possible variables.
letters_to_use = ["a","b","c","d","e","f","g","h"]
letters_to_use.extend(["i","j","k","l","m","n","o","p","q"])
letters_to_use.extend(["r","s","t","u","v","w","x","y","z"])
letters_to_use.extend(["ar","as","at","au","av","aw","ax","ay","az"])
letters_to_use.extend(["br","bs","bt","bu","bv","bw","bx","by","bz"])
letters_to_use.extend(["cr","cs","ct","cu","cv","cw","cx","cy","cz"])
letters_to_use.extend(["dr","ds","dt","du","dv","dw","dx","dy","dz"])
letters_to_use.extend(["er","es","et","eu","ev","ew","ex","ey","ez"])
letters_to_use.extend(["fr","fs","ft","fu","fv","fw","fx","fy","fz"])

#We define a function that deliver a list with $n$ variables

def variables(n):
    return letters_to_use[:n]

#The next function create a list with cuadratic terms for n variables.    
def listaquad(n):
    return [f'{var}^2' for var in variables(n)]


#Construct a list with k terms within a form like our cuadratic formulaes from
# n variables split in groups of m variables in each equation.
def quadterms(m,n):
    terms = []
    k = int((n-(n%m))/m)
    if n%m==0:
        for i in range(k):
            sumquad = '+'.join(listaquad(n)[i*m:(i+1)*m])
            terms.append(sumquad)
    else:
        for i in range(k+1):
            sumquad = '+'.join(listaquad(n)[i*m:(i+1)*m])
            terms.append(sumquad)
    
    return terms

#Create a list within the n*(n-1) products between variables.

def listacros(n):
    prodcros = []
    for var in variables(n):
        for var2 in variables(n):
            if var2==var:
                continue
            else:
                cros = f'({var}*{var2})^2'
                prodcros.append(cros)
    
    return prodcros

#Gives a list within k cuadratics formulaes from n variables in groups of m
#variables in each equation.
def crosterms(m,n):
    cterms = []
    k = int((n-(n%m))/m)
    if n%m==0:
        for i in range(k):
            sumcros = '+'.join(listacros(n)[i*m:(i+1)*m])
            cterms.append(sumcros)
    else:
        for i in range(k+1):
            sumcros = '+'.join(listacros(n)[i*m:(i+1)*m])
            cterms.append(sumcros)
    
    return cterms

#Finally create a string with a formulae that we will send to Mathematica
def build_formula(k,m,n,p,s):
    formula1 = "("+"==1/6&& ".join(quadterms(m,n)[:s])+"==1/6)"
    formula2 = "("+"==1/6&&".join(crosterms(k,n))+"==1/6)"
    return "Exists[{"+",".join(variables(p))+"}, "+formula1+"&& "+formula2+"]"

formula = build_formula(4,2,4,2,2)



    