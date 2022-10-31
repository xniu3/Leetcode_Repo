def complementaryPairs(words):
    ret = 0
    hashmap = dict()
    for word in words:
        bitmask = 0
        for char in word:
            print("char is ",char,"(ord(char) - ord('a')) is ",(ord(char) - ord('a')), 1<<(ord(char) - ord('a')))
            bitmask ^= 1<<(ord(char) - ord('a'))
        print("Bitmask is ",bitmask)
        # bitmask 就是字符串的map，
        if bitmask not in hashmap:
            hashmap[bitmask] = 1
        else:# bitmask in hashmap
            hashmap[bitmask] += 1
        
        for i in range(ord('a'), ord('z')):
            char = chr(i)
            temp = bitmask ^ 1<<(ord(char) - ord('a'))
            # print("temp is ",temp)
            if temp in hashmap:
                ret += hashmap[temp]
    return ret
        # check bitmask 是否在hash_map（key: bitmask, value: count)中
        # 对于26位来说各异或一次，并判断是否在hash_map中
        ## 如果在就加上对应count的数目到result中
# words = ["abc" , "abcd" , "bc" , "adc"]
'''
for word in words:
    # 字符串转换为integer便于位运算
    bitmask = 0
    for c in word:
        bitmask ^= (1<<(ord(c) - ord('a'))
    # check bitmask 是否在hash_map（key: bitmask, value: count)中
    # 对于26位来说各异或一次，并判断是否在hash_map中
    # 如果在就加上对应count的数目到result中
    # ["4"]
'''
# words = [ "ball","all","call", "bal"]
words = ["aac",'ab', "d"]
#["abc", "abcd", "bc", "adc"]
results = complementaryPairs(words)
print("results is ",results)