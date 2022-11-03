def rectangles(operation):
    from heapq import heappush, heappop, heapify
    ret = list()
    heapa, heapb = list(), list()
    for opera in operation:
        a, b = opera[1], opera[2]
        if opera[0] == 0:
            if a > b:
                b , a = a , b
            heappush(heapa, a)
            heappush(heapb, b)
        else:# opera[1] == 1
            if a > b:
                b , a = a , b
            if a <= heapa[0] and b <= heapb[0]:
                ret.append(True)
            else:
                ret.append(False)

    return ret


operation1 = [
    [0, 3, 3],
    [0, 5, 2],
    [1, 3, 2],
    [1, 2, 4],
]
print(rectangles(operation1))
