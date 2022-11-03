

def MaxXOR(n:int):
    bin_str = bin(n)
    max_val = 2 ** (len(bin_str) - 2) - 1
    print("max_val is",max_val)
    # 注意：正确解法在下面但会超时，快速的解法是返回max_val - 1
    # return max_val - 1
    v = 0
    maxindex , maxv = 0 , 0
    for i in range(n , max_val):
        v ^= i
        if v > maxv:
            maxindex = i
            maxv = v
    return maxindex

print(MaxXOR(100000000))

