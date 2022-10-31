def MaximumScore(array,k):
    from heapq import heapify, heappush, heappop
    ret = list()
    newarray = [-i for i in array]
    heapify(newarray)
    for i in range(k):
        temp = heappop(newarray)
        ret.append(-temp)
    return ret
array = [4,6,-10, -1, 10,-20]

retlist = MaximumScore(array,4)
print("retlist is ",retlist)

