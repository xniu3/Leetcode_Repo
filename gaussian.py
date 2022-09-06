from scipy.stats import erlang,expon
from scipy.stats import norm
g = lambda x:1
g1 = lambda x:x**2
# mean=expon.expect(g,args=[8],scale=1/10)   #计算E(Y)
mean = norm.expect(g,loc = 2,scale=1)
# mean2 = expon.expect(g1,scale=1/2.3)
# print(mean,mean2)
# print(mean - mean2**2)

print(mean)