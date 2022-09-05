from re import L


class Solution:
    def __init__(self) -> None:
        pass
    def issub(self,str1:str,str2:str):
        i , j = 0 , 0
        l1 , l2 = len(str1) , len(str2)
        # if len(str1) < len(str2):
        if l1 < l2:
            return False
        while i < l1:
            if str1[i] == str2[j]:
                j += 1
            i += 1
        if j == l2:
            return True
        else:
            return False

if __name__ == '__main__':
    solu = Solution()
    ret = solu.issub('adcb','abc')
    print(ret)