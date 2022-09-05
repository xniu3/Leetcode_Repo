class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        len1 , len2 = len(num1) , len(num2)
        total = 0
        for i in range(len2):
            total *= 10
            total += self.multiply1(num1, num2[i])
            
        return total
    def multiply1(self,nums1:str, nums2):
        if nums2 == '0':
            return 0
        else:
            val2 = ord(nums2[0]) - ord('0')
            add = 0
            summer = 0
            n1 = len(nums1)
            for i in range(0,n1):
                summer *= 10
                val1 = ord(nums1[i]) - ord('0')
                summer += val2 * val1
                
            return summer

if __name__ == "__main__":
    Solu = Solution()
    ret = Solu.multiply('123','456')
    print(ret)