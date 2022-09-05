# 答案区
from scipy import integrate
from math import exp , log2, log, sin,cos
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
# result = integrate.quad(f,0,1,args=(1,2,3))
result = integrate.quad(f1,0,5)
print("result is ",result)