from functools import cmp_to_key


class Solution:
    from typing import List
    def compare(self,str1:str, str2:str):
        val1 = int(str1 + str2)
        val2 = int(str2 + str1)
        if val1 > val2:
            return 1
        elif val2 > val1:
            return -1
        else:
            return 0
    def largestNumber(self, nums: List[int]) -> str:
        numstr = [str(i) for i in nums]
        numstr.sort(key=cmp_to_key(self.compare))
        print("numstr is before reverse",numstr)
        numstr.reverse()
        print("numstr is ",numstr)
        


if __name__ == '__main__':
    Solu = Solution()
    ret = Solu.largestNumber([34323,3432])
    print(ret)