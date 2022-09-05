class Solution:

    from typing import List
    def isPossible(self, target: List[int]) -> bool:
        from heapq import heappush,heappop,heapify
        summer = 0
        
        stack = list()
        heapify(stack)
        for i in range(len(target)):
            
            heappush(stack, - target[i])
            summer += target[i]
            # print("stack is ",stack)
            # print("target value is ",target[i], "summer is ",summer)
        while stack:
            x = - heappop(stack)
            y = - stack[0]
            # print("x is ",x,"y is ",y )
            if x == 1:
                break
            if 2 * x - summer < 1:
                return False
            left = summer - x 
            print("left is",left)
            if y == 1:
                k = (x - y + left - 1) // left
            else:
                k = (x - y) // left + 1
            if x <= 0:
                return False
            summer -= k * left
            heappush(stack,-x)
        return True


if __name__ == "__main__":
    solu = Solution()
    newlist = [2,90000002]
    ans = solu.isPossible(newlist)
    print(ans)