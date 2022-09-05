from typing import List
class Solution:
    def largestRectangleArea(self, heights:List) -> int:
        stack = list()
        length = len(heights)
        dp = [0] * length

        for i in range(length):
            height = heights[i]
            while stack and stack[-1] < height:
                stack.pop()
            stack.append(height)

if __name__ == '__main__':
    Solu = Solution()
    ret = Solu.largestRectangleArea([2,1,5,6,2,3])
    print(ret)