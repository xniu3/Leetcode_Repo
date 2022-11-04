
def shortestPalindrome(s:str):
    n = len(s)
    fail = [-1] * n
    for i in range(1, n):
        j = fail[i - 1] 
        
        while j != -1 and s[j + 1]!=s[i]:
            j = fail[j]
        if s[j + 1] == s[i]:
            fail[i] = j + 1
    print("fail is ",fail)
    best = -1
    for i in range(n - 1, -1 , -1 ):
        while best != -1 and s[best + 1] != s[i]:
            best = fail[best]
        if s[best + 1] == s[i]:
            best += 1
    add = ("" if best == n - 1 else s[best + 1:] )
    return add[::-1] + s
    
print(shortestPalindrome('aacecaaa'))


'''
输入: s = "aacecaaa"
输出："aaacecaaa"

'''
