
from operator import le


class Solution:
    def __init__(self) -> None:
       pass 
    def swap(self,a,b) -> bool:
        hashtable1 , hashtable2 = dict() , dict()
        match1 , match2 = dict() , dict()
        for chara in a:
            if chara not in hashtable1:
                hashtable1[chara] = 1
            else:
                hashtable1[chara] += 1
        for chara in b:
            if chara not in hashtable2:
                hashtable2[chara] = 1
            else:
                hashtable2[chara] += 1
        for key,value in hashtable1.items():
            if value % 2 == 0:
                continue
            match1[key] = value
            print("key, value is ",key,value)
        for key,value in hashtable2.items():
            if value % 2 == 0:
                continue
            match2[key] = value
            print("key, value is ",key,value)    
        print(match1)
        print(match2)
        return False
    def isPalindrome(self,s:str) -> bool:
        ret = True
        length = len(s)
        slow , fast =  0 , length - 1
        while slow < fast:
            if s[slow] == s[fast]:
                slow += 1
                fast -= 1
            else:
                ret = False
                break
                # return False
        print("here")
        if ret:
            return True
        def segment(s,low , high):
            while low < high:
                if s[low] == s[high]:
                    low += 1
                    high -= 1
                else:
                    return False
                
            return True
        ret = True
        while slow < fast:
            if s[slow] == s[fast]:
                slow += 1
                fast -= 1
            else:
                return segment(s,slow + 1, fast) or segment(s,slow, fast - 1)
        # return ret
        return True
solu = Solution()
a = "dabccd"
b = "dccdfg"
# solu.swap(a,b)
print(solu.isPalindrome(a))



