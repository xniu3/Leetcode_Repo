class NumArray:
    from typing import List
    def __init__(self, nums: List[int]):
        self.prefix = list()
        self.prefix.append(0)
        for num in nums:
            temp = self.prefix[-1] + num
            self.prefix.append(temp)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right] - self.prefix[left]
if __name__ == '__main__':
    Num = NumArray([-2,1,3,5,7])
    ret = Num.sumRange(0,2)
    print(ret)