def complementaryPairs1(words):
    ret = 0
    hashmap = dict()
    for word in words:

        bithash = 0

        for char in word:
            bithash ^= 1<<(ord(char) - ord('a'))
        if bithash not in hashmap:
            hashmap[bithash] = 1
        else:
            hashmap[bithash] += 1
        
        for i in range(ord('a'), ord('z')):
            char = chr(i)
            temp = bithash ^ 1 <<(ord(char)- ord('a'))
            if temp in hashmap:
                ret += hashmap[temp]
    
    return ret

words = ['aabb','ab']# ["abc", "abcd", "bc", "adc"]#["ball", "all", "call", "bal"]
result = complementaryPairs1(words)
print(result)


