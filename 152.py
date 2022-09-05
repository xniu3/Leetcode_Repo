class Solution:
    from typing import List
    def __init__(self) -> None:
        pass

    def maxval(self, nums):
        maxF , minF , ans = nums[0] , nums[0] , nums[0]
        n = len(nums)
        for i in range(1,n):
            mx , mn = maxF, minF
            #maxF = max(mx * nums[i], max(nums[i], mn * nums[i]))
            # minF = min(mn * nums[i], min(nums[i], mx * nums[i]))
            maxF = max(mx * nums[i] , mn * nums[i] , nums[i])
            minF = min(mn * nums[i] , mx * nums[i] , nums[i])
            print("maxf is ",maxF, "minF is ",minF)
            ans = max(maxF, ans)
        return ans

if __name__ == "__main__":
    Solu = Solution()
    arr = [2,3,-2,4]
    ret = Solu.maxval(arr)
    print(ret)