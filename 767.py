import collections 
from heapq import heapify, heappop, heappush
def reorganizeString(s: str) -> str:
    if len(s) < 2:
        return s
    
    length = len(s)
    counter = collections.Counter(s)
    print("counter is ",counter.items())
    maxCount = max(counter.items(),key=lambda x:x[1])[1]
    queue = [(-x[1],x[0]) for x in counter.items()]
    heapify(queue)
    # print(maxCount)
    # print(heappop(queue))
    ans = list()
    while len(queue) > 1:
        _ , letter1 = heappop(queue)
        _ , letter2 = heappop(queue)
        # 根据Python的PEP8编码规范，对于用不到的循环计数变量，应该使用下划线代替
        ans.extend([letter1, letter2])
        counter[letter1] -= 1
        counter[letter2] -= 1
        if counter[letter1] > 0:
            heappush(queue, (-counter[letter1],letter1))
        if counter[letter2] > 0:
            heappush(queue, (-counter[letter2],letter2))
    if queue:
        ans.append(queue[0][1])
    return "".join(ans)   
reorganizeString('aaabcccc')