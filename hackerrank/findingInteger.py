
from heapq import heappush, heappop, heapify
def findingInteger(n:int, k:int, array:list):
    def findtopk(array,k):
        temp = array[:]
        ret = 0
        for _ in range(k):
            ret = -heappop(temp)
        return ret
    oldtemp = array[:k]
    temp = [-i for i in oldtemp]
    ret = list()
    heapify(temp)
    value = findtopk(temp,k)
    ret.append(value)
    for i in range(k,n):
        temp.append( -array[i])
        print("temp is ",temp)
        heapify(temp)
        value = findtopk(temp,k)
        ret.append(value)
    return ret


print(findingInteger(4,2,[4,2,1,3]))


