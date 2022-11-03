def isPalin(string:str)-> bool:
    if not string:
        return True
    else:
        slow , fast = 0 , len(string) - 1
        while slow < fast:
            if s[slow] != s[fast]:
                return False
            else:
                slow += 1
                fast -= 1
        return True

isPalin("aab")