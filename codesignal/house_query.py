def solution(houses, queries):
    
    houselist = []
    prev = None
    ret = list()
    houses.sort()
    print(houses)
    for index, house in enumerate(houses):
        if not houselist:
            houselist.append([house])
        if prev == None:
            prev = house
        else:
            if prev + 1 != house:
                houselist.append([house])
                prev = house
            else:
                houselist[-1].append(house)
                prev = house
        # print("houselist is now",houselist)
    # print(houselist)
    def binary_search(value):
        slow , fast = 0 , len(houselist)
        while slow < fast:
            mid = (slow + fast) // 2
            if houselist[mid][0] == value:
                return mid
            elif houselist[mid][0] < value:
                slow = mid + 1
            else:
                fast = mid - 1
        return slow
    for index, query in enumerate(queries):
        # print("index is ", index, "query is ", query)
        # print("houselist is now", houselist)
        possible = binary_search(query)
        if possible >= len(houselist) or query < houselist[possible][0]:
            possible -= 1
        # print(possible)
        if query == houselist[possible][0]:
            if len(houselist[possible]) == 1:
                houselist.remove(houselist[possible])
            else:
                houselist[possible].remove(query)
        elif query == houselist[possible][-1]:
            if len(houselist[possible]) == 1:
                houselist.remove(houselist[possible])
            else:
                houselist[possible].remove(query)
        else:
            split = houselist[possible].index(query)
            # print("split is ",split)
            list1 = houselist[possible][:split]
            list2 = houselist[possible][split + 1:]
            # print("list1 is ",list1)
            # print("list2 is ",list2)
            houselist.remove(houselist[possible])
            houselist.insert(possible,list2)
            houselist.insert(possible,list1)
            
            
        ret.append(len(houselist))
            
    return ret
