def convert(num:int,n):
    dp = [0] * n
    point = n - 1
    while num >= 1:
        digit = num % 2
        dp[point] = digit
        point -= 1
        num >>= 1
    return dp
ret = convert(3,2)

print(ret)
