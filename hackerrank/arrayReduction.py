
from collections import defaultdict , deque
from math import ceil
def findTotalCost(array:list):
    n = len(array)
    queue = deque(array)
    totalcost = 0
    for i in range(n - 1):
        minval = queue.popleft()
        maxval = queue.pop()
        queue.append(minval + maxval)
        addition = ceil((minval + maxval) / (maxval - minval + 1))
        print("addition is ",addition)
        totalcost += addition
    return totalcost





print(findTotalCost([2, 3, 4, 5, 7 ]))