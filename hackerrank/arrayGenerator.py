def arrayGenerator(array, l , r):
    n = len(array)
    brray = [0] * n
    diff = 0
    for i in range(n):
        cur = max(l,array[i]) + diff
        if cur > r:
            return -1
        else:
            brray[i] = cur
            diff += 1
    return brray


array = [1,2,1,2]
l , r = 1, 10
array=[15,97,32,46,18,16,13,11,44,56]
l=3
r=323
ret = arrayGenerator(array, l ,r)
print(ret)
