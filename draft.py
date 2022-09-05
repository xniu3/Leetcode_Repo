from math import exp
def calc():
    return sum(x ** 2 for x in range(0,11))
def comment(x):
    ret = 1
    for i in range(1,x + 1):
        ret *= i
    return ret
def calc2(n,p,k):
    return comment(n) * (p ** k) * ((1-p) ** (n - k)) / (comment(k) * comment(n - k))
def expression(x):
    return 4 - 7 * x - (2- 3 * x) ** 2
def poss(lam,t, n):
    return (lam * t) ** n * exp(-lam*t) / comment(n)
def poss2(lam, x):
    return (lam) ** x * exp(-lam) / comment(x)
def pascal(x,k,p):
    return comment(x-1) * (p ** k) * ((1-p) ** (x - k)) / (comment(x - k ) * comment(k - 1))
if __name__ == "__main__":
    # print(expression(0.23))
    # calc2 n p k
    # print(calc2(18,0.8,16) + calc2(18,0.8,17) + calc2(18,0.8,18) )
    # print(calc2(8, 0.5, 1) + calc2(8, 0.5, 7))
    # print(1 - poss(6,1/7,0) - poss(6,1/7,1) - poss(6,1/7,2))
    # print(1- poss2(3.96,0) - poss2(3.96,1))
    # print(pascal(10,6,0.72))
    print(poss2(0.77,3))