import numpy as np
from random import *

def create_coeffs():
    coeffs = list(range(-5, 6, 1))
    coeffs.remove(0)

    a = choice(coeffs)
    b = randint(-5, 5)
    c = randint(-5, 5)
    
    if b==c and b==min(coeffs):
        c+=1
    if b==c and b==max(coeffs):
        c-=1
        
    return {"a":a,
         "b":b,
         "c":c}

def f(x, coeffs):
    return coeffs["a"]*x**2+coeffs["b"]*x+coeffs["c"]

find_h = lambda a, b: -b/(2*a)
find_k = lambda h: f(h, coeffs)

def create_eq_str(coeffs):
    return r"$y=({a})x^2+({b})x+({c})$".format(**coeffs)

def create_hk_str(coeffs):
    h = find_h(coeffs["a"], coeffs["b"])
    k = find_k(h, coeffs)
    coeffs.update({"h":h, "k":k})
    
    return r"$y={a}(x-({h}))^2+({k})$".format(**coeffs)

def decide_correct():
    return (randint(0,1), randint(0,1)) 

def create_wrong(coeffs):    
    a_factor = choice([-1, -1/2, 1/2, 2])
    c_add_list = list(range(1, 3)) + list(range(-3, 1))
    c_add = choice(c_add_list)
    coeffs.update({"a":coeffs["a"]*a_factor, "c":coeffs["c"]+c_add})
    return coeffs

