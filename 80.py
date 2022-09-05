class Solution:
    from typing import List
    def removeDuplicates(self, nums: List[int]) -> int:
        slow , fast = 2 , 2
        if len(nums) <= 2:
            return len(nums)
        n = len(nums)
        while fast < n:
            print("slow is ",slow,"fast is ",fast)
            print("val slow-2 is ",nums[slow - 2] ,"val fast is ", nums[fast])
            if nums[slow - 2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
                
            fast += 1
        return slow


if __name__ == "__main__":
    Solu = Solution()
    ret = Solu.removeDuplicates([1,1,1,2,2,3])
    print(ret)