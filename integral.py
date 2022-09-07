# 答案区
from scipy import integrate
from math import exp , log2, log, sin,cos,pi
import numpy as np
def f(x):
    return x+1
def g(x):
    return log(x)+2
def h(x):
    return f(x) / g(x)
# v,err = integrate.quad(h,1,2)
# print(v)  #err为误差项
def f(x,a): #a is a parameter, 
            # x is the variable I want to integrate over
    return a*x
def f(x,a,b,c):  #a is a parameter, x is the variable I want to integrate over
    return a*x + b + c
def f1(x):
    return x**2 * (3 * 5 ** 2/250 - 3 * x ** 2/250)
def f2(x):
    return exp(-x**2/2)/(2*pi)**0.5
def f3(x):
    # a = 17
    miu , sigma = 2500 , 49 * 50**0.5
    return exp(-(x-miu)**2/(2*sigma**2))/(2*pi*sigma**2)**0.5
# result = integrate.quad(f,0,1,args=(1,2,3))
# result = integrate.quad(f3,0,5)
result = integrate.quad(f3,-np.inf,2200)
# result = integrate.quad(f3,67,69)
print("result is ",1 - result[0])
'''
result1 = integrate.quad(f3,-np.inf,5)
result2 = integrate.quad(f3,-np.inf,2)
result3 = integrate.quad(f3,-np.inf,0)
result3 = integrate.quad(f3,-np.inf,9)
result4 = integrate.quad(f3,-np.inf,-3)
'''
