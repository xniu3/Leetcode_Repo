def solution(a):
    if not a:
        return a
    def digit2str(a):
        if a < 9:
            return [str(a)]
        else:
            ret = []
            while a >= 10:
                ret.append(str(a % 10))
                a //= 10
            ret.append(str(a))
            return ret
    total = []
    for num in a:
        digit = digit2str(num)
        total += digit
    print(total)
    hashtable = dict()
    for num in total:
        if num not in hashtable:
            hashtable[num] = 1
        else:
            hashtable[num] += 1
    print(hashtable)
    maxlist = []
    maxval = 0
    for key,value in hashtable.items():
        key = int(key)
        if value > maxval:
            maxlist = [key]
            maxval = value
        if value == maxval:
            maxlist.append(key)
    maxlist.sort()
    return list(set(maxlist))

print(solution([25, 2, 3, 57, 38, 41]))



