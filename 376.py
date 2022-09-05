class Solution:
    from typing import List
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp_up = [0] * n
        dp_down = [0] * n
        dp_up[0] = 1
        dp_down[0] = 1
        for i in range(1,n):
            if nums[i] > nums[i - 1]:
                dp_up[i] = max(dp_up[i - 1] ,dp_down[i - 1] + 1)
                dp_down[i] = dp_down[i - 1]
            else:
                dp_down[i] = max(dp_up[i - 1] + 1 , dp_down[i - 1])
                dp_up[i] = dp_up[i - 1]
                # down_last = nums[i]
                # up_last = nums[i]

        print("dp_up is ",dp_up)
        print("dp_down is ",dp_down)
        return max(dp_up[-1],dp_down[-1])


if __name__ == '__main__':
    Solu = Solution()
    nums = [1,17,5,10,13,15,10,5,16,8]
    ret = Solu.wiggleMaxLength(nums)
    print(ret)