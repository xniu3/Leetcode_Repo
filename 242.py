

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table1 = self.convert(s)
        table2 = self.convert(s)
        print("table1 is ",table1)
        print("table2 is ",table2)
        for key in table1.keys():
            if key not in table2:
                return False
            if table1[key] != table2[key]:
                return False
        for key in table2.keys():
            if key not in table1:
                return False
            if table1[key] != table2[key]:
                return False
        return True
    def convert(self,s:str):
        hashtable = dict()
        for char in s:
            if char not in hashtable:
                hashtable[char] = 1
            else:
                hashtable[char] += 1
        return hashtable



if __name__ == '__main__':
    Solu = Solution()
    s = "rat"
    t = "car"
    ret = Solu.isAnagram(s,t)
    print(ret)