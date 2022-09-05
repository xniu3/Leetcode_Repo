class Solution:
    from typing import List
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from heapq import heappush,heappop,heapify
        hashtable = dict()
        stack = list()
        for num in nums:
            if num not in hashtable:
                hashtable[num] = 1
            else:
                hashtable[num] += 1
        for key,value in hashtable.items():
            print("key is ",key,"value is ",value)
            heappush(stack,(-value,key))
        for i in range(k):
            temp = heappop(stack)#[1]
            key = temp[1]
            print("key is ",key)
        print(stack)


if __name__ == '__main__':
    Solu = Solution()
    ret = Solu.topKFrequent([1,1,1,3,2,2,2,3],2)
    print(ret)