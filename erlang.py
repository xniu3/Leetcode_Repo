'''from math import log2
from scipy import optimize
def f(x):
    return  x*log2(x) + (0.55-x)*log2(0.55-x)



maximum = optimize.fminbound(f, 0, 0.55)
print(maximum)
'''
from scipy.stats import erlang,expon                #导入norm
# g=lambda x: 1/x                         #设置函数Y=g(X)=5X^2
g = lambda x:x**4
g1 = lambda x:x**2
# mean=expon.expect(g,args=[8],scale=1/10)   #计算E(Y)
mean = expon.expect(g,scale=1/2.3)
mean2 = expon.expect(g1,scale=1/2.3)
print(mean,mean2)
print(mean - mean2**2)
