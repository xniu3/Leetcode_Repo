class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lens, lent = len(s) , len(t)
        hashtable = dict()
        dp = [float('inf')] * lens
        for j in range(lent):
            hashtable[t[j]] = 0
        print("initial hashtable is ",hashtable)
        slow , fast = 0 , 0
        answer = list()
        while fast < lens:
            print("s fast is ",s[fast])
            if s[fast] in hashtable:
                hashtable[s[fast]] += 1
                print("hashtable is ",hashtable)
                if 0 not in hashtable.values():
                    while 0 not in hashtable.values() and slow <= fast:
                        print("slow is ",slow)
                        if s[slow] not in hashtable:
                            print("s[slow]",s[slow],"not in hashtable")
                            slow += 1
                        else:
                            print("s[slow]", s[slow], "is in hashtable" )
                            hashtable[s[slow]] -= 1
                    answer.append([slow, fast])
                    hashtable[s[slow]] += 1
            fast += 1
        print(answer)
        return answer


if __name__ == '__main__':
    Solu = Solution()
    ret = Solu.minWindow(s = "ADOBECODEBANC", t = "ABC")
    print(ret)