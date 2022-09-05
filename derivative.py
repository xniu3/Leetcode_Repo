from sympy import *
from math import exp , log2, log, sin,cos
x,y = symbols("x y")
result = diff(x**23,x)
print(result)