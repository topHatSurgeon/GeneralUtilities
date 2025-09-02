#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 29 11:09:16 2025

@author: nayandusoruth
"""

import sympy as sy
#from sympy import *
from sympy import init_printing
import matplotlib as plt
init_printing()
from IPython.display import display
import numpy as np

"""
This module is intended to make symbolic maths handling via the sympy library easier

sympy docs:
    https://docs.sympy.org/latest/tutorials/intro-tutorial/features.html

module wishlist:
    - Error propagation calculator
    - PDE handler?
    
    
sympy library recap/summary:
    - object types:
    - symbols/variables - x, y, z = symbols('x y z')
    - main "object" of sympy is "expression" - expression = function(symbols)
    - Eq object - Eq(expression1, expression2) is equivilant to expression1 = expression2
    - also has set object
    useful functions:
        - simplification functions - expand(), factor()
        - limit function - limit(expression, x, 0)
        - derivative function - diff(expression, x)
        - integral functions - integrate(expression, x) and integrate(expression, (x, lowerBound, upperBound))
    useful solver functions:
        - algebraic solver - solve(expression, x) - apparently solveset(expression, x, domain=S.reals)
        - ODE solver:
            y = function('y') 
            dsolve(Eq(differentials(y(t)), inhomogenousTerm), y(t))
    matrix methods:
        - can construct matrices, perform simple matrix operations (I.E, addition, multiplication...), perform complex operations (I.E, RREF, eigenvectors...)
    

"""

# sympy expression summation - </verified/>
def sumExpressions(expressions):
    """utility function - sums sympy expressions together"""
    returnable = 0
    for i in expressions:
        returnable = returnable + i
    return returnable

# computes single term in error propagation series - </verified/>
def errorPropagationTerm(expression, variable):
    """Error propagation term function - computes error expression due to 'variable' in 'expression' and returns error term"""
    standardDeviation = sy.symbols(str(str(variable) + "_err"))
    errorTerm = (standardDeviation * expression.diff(variable))**2
    return errorTerm
    
# computes all error terms in expression as a function of all variables - </verified/>
def errorPropagate(expression, returnSymbols=False):
    """Error propagation function - returns list of all error propagation terms in an expression for all variables"""
    symbols = list(expression.free_symbols)
    expressions = np.array([errorPropagationTerm(expression, symbols[0])])
    
    for i in range(1, len(symbols)):
        expressions = np.append(expressions, errorPropagationTerm(expression, symbols[i]))

    if(returnSymbols):
        return expressions, symbols
    return expressions



x, y, z = sy.symbols('x y z')
expression = x**2+y**3 + z

#errorTerm = errorPropagationTerm(expression, x)
#sy.pprint(errorTerm)
print(type(expression))
errorTerms = errorPropagate(expression)
print(errorTerms)
errors = sumExpressions(errorTerms)

sy.pprint(errors)
# ====================================================================================================================
# general testing and experimentation 
# ====================================================================================================================

# algebraic solver experiment
"""
x, a = sy.symbols('x a')
expression = x**2

equation = sy.Eq(expression, -1)
print(sy.solveset(equation, x, domain=sy.S.Complexes))
pprint(expression.diff(x))
"""
# linsolve experiments


# dsolve experiment
"""
x = sy.symbols('x')
f = sy.symbols('f', cls=sy.Function)
diffEq = sy.Eq(f(x).diff(x, x) + f(x).diff(x),0)
sy.pprint(diffEq)
#display(diffEq)
initialCond = {f(0):0, f(x).diff(x).subs(x,0):1}
sol = sy.dsolve(diffEq, f(x), ics=initialCond)
sy.pprint(sol)
#print(sol)
"""



# PDE seperation experiment
"""
x, y = symbols('x y')
f = symbols('f', cls=Function)
diffEq = Eq(f(x, y).diff(x)+f(x,y).diff(y),0)
pprint(diffEq)
X, Y = map(Function, 'XY')
ODEs = sy.solvers.pde.pde_separate(diffEq, f(x,y), [X(x),Y(y)])
print(ODEs)
c = symbols('c')
diffEq0 = Eq(ODEs[0], c)
diffEq1 = Eq(ODEs[1], c)
#pprint(diffEq0)
#pprint(diffEq1)
sol0 = sy.dsolve(diffEq0, X(x))
sol1 = sy.dsolve(diffEq1, Y(y))
#pprint(sol0)
#pprint(sol1)
#sol = dsolve(diffEq)
#pprint(sol)
#print(sol0.rhs)
fullSol = sol0.rhs * sol1.rhs
C_1=list(fullSol.free_symbols)[1]
A = symbols('A')
fullSol = fullSol.subs(C_1**2, A)
pprint(fullSol)
fullSol = simplify(fullSol)
pprint(fullSol)
"""

# PDE solver """experiment
"""
x, y = symbols('x y')
f = symbols('f',cls=Function)
u = f(x,y)
ux = u.diff(x)
uy = u.diff(y)
diffEq = Eq(ux+uy, u)
sol =sy.solvers.pde.pdsolve(diffEq, u)
print(sol)
"""

# matrix testing
"""
M = Matrix([[1,2],[2,1]])
N = Matrix([[0,1],[1,1]])
pprint(M)
print(M.eigenvals())
pprint( M.eigenvects())
"""
