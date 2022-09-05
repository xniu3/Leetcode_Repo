class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        lens , lenp = len(s) , len(p)
        dp = [[False] * (lenp + 1) for _ in range(lens + 1)]
        dp[0][0] = True
        marker = 0
        for j in range(1,lenp + 1):
            if marker == 1:
                dp[0][j] = False
            if p[j -1] == '*':
                dp[0][j] = True
            if p[j - 1] != '*' and p[j-1] != '?':
                dp[0][j] = False
                marker = 1
            
        for i in range(1,lens + 1):
            dp[i][0] = False
        for i in range(1 , lens + 1):
            for j in range(1 , lenp + 1):
                if p[j - 1] != '*' and p[j - 1] != '?':     
                    if s[i -1 ] == p[j - 1]:
                        dp[i][j] = dp[i -1][j -1]
                    else:
                        dp[i][j] = False
                elif p[j -1 ] == '?':
                    dp[i][j] = dp[i - 1][ j - 1]
                else:
                    temp = False
                    for k in range(i + 1):
                        temp = temp or dp[i - k][j - 1]
                    dp[i][j] = temp
        print(dp)
        return dp[-1][-1]
        
if __name__ == '__main__':
    Solu = Solution()
    s = "aab"
    p = "c*a*b"
    ret = Solu.isMatch(s,p)
    print(ret)