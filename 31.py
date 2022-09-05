class Solution:
    from typing import List
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #v for i in range(nums)
        n = len(nums)

        res = list()

        
        def dfs(pos):
            if pos > n:
                return
            elif pos == n:
                res.append(nums)
            else:
                
                dfs(pos + 1)
            dfs(pos + 1)
if __name__ == "__main__":
    Solu = Solution()
    ans = Solu.nextPermutation([1,2,3])
    print(ans)
        
        
        