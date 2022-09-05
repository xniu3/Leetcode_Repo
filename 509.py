def fib(n: int) -> int:
    num1 , num2 = 0 , 0 
    if n == 0:
        return 0
    num1 = 1
    ret = 1
    for i in range(n - 1):
        
        ret = num1 + num2
        num2 = num1
        num1 = ret
        print("ret is ",ret)
    return ret

if __name__ == "__main__":
    ret = fib(5)
    print("result is ",ret)