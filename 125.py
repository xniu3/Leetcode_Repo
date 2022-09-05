class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        slow , fast = 0 , n - 1
        while slow < fast:
            print("slow is ",slow , 'Fast is ', fast)
            while slow < fast and (not s[slow].isalpha() and not s[slow].isdigit()):
                slow += 1
            while slow < fast and (not s[fast].isalpha() and not s[fast].isdigit()):
                fast -= 1
            print(" After check slow is ",slow , 'Fast is ', fast)
            if s[slow].lower() != s[fast].lower():
                return False
            else:
                slow += 1
                fast -= 1
        return True
if __name__ == '__main__':
    Solu = Solution()
    s = '0P'
    #"A man, a plan, a canal: Panama"
    ret = Solu.isPalindrome(s)
    print(ret)