from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ret = list()
        sequence = nums[:]
        print("sequence is ",sequence)
        n = len(nums)
        def dfs(i:int):
            if i > n:
                return 
            if i == n:
                ret.append(sequence[:])
                return 
            dfs(i + 1)
            for j in range(i + 1 , n):
                sequence[i] , sequence[j] = sequence[j] , sequence[i]
                dfs(i + 1)
                sequence[i] , sequence[j] = sequence[j] , sequence[i]
        dfs(0)
        return ret


if __name__ == '__main__':
    Solu = Solution()
    ret = Solu.permuteUnique([1,2,3])
    print(ret)