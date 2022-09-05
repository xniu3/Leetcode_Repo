from heapq import heapify, heappush, heappop
nums = [1,2,3,4,4,5]
heapify(nums)

import heapq
from typing import List
from collections import defaultdict
from heapq import heappush, heappop, heappush
def isPossible(nums: List[int]) -> bool:
    mp = defaultdict(list)
    for x in nums:

        if queue := mp.get(x - 1):
            print("queue is ",queue)
            print("mp is ",mp)
            prevLength = heapq.heappop(queue)
            heapq.heappush(mp[x], prevLength + 1)
        else:
            heapq.heappush(mp[x], 1)
    
    return not any(queue and queue[0] < 3 for queue in mp.values())

ret = isPossible(nums)
print(ret)