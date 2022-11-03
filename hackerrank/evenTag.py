def evenTag(array):
    length = len(array)
    odd_max = None
    even_max = None
    ret = 0
    for index, value in enumerate(array):
        if value > 0:
            if value % 2 == 0:
                if even_max == None:
                    even_max = value
                else:
                    even_max += value
                if odd_max != None:
                    odd_max += value
            else:# value % 2 == 1
                if even_max == None:
                    odd_max = value
                else:
                    temp = odd_max
                    odd_max = even_max + value
                    if temp != None:
                        even_max = temp + value
        ret = ret if even_max < ret else even_max
    return ret
def evenTag2(array):
    length = len(array)
    positive_sum = 0
    min_odd = None
    for value in array:
        if value >= 0:
            positive_sum += value
        if value % 2 != 0:
            min_odd = value if value >= 0 else -value
    if positive_sum % 2 == 0:
        return positive_sum
    else:
        return positive_sum - min_odd
print(evenTag([2,3,6,-5,10,1,1 ]))
print(evenTag2([2,3,6,-5,10,1,1 ]))