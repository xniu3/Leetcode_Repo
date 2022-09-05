def isPalin(s:str):
    n = len(s)
    if n == 1:
        return True
    if n == 2:
        return s[0] == s[1]
    
    mid = n // 2 
    p1 , p2 = mid - 1 , mid
    print(p1,p2)
    if n % 2 == 1:
        p2 += 1
    while p2 < n:
        if s[p1] !=s[p2]:
            return False
        p1 -= 1
        p2 += 1
    return True
print(isPalin('abba'))