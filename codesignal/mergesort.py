
from syslog import LOG_LOCAL2


def mergesort(array):
    if not len(array) > 1:
        return
    mid = len(array) // 2
    list1 = array[:mid]
    list2 = array[mid:]
    mergesort(list1)
    mergesort(list2)

    p1 , p2 = 0 , 0
    list3 = list()
    len1 , len2 = len(list1) , len(list2)
    p = 0
    while p1 < len1 or p2 < len2:
        if p1 == len1:
            array[p] = list2[p2]
            # list3.append(list2[p2])
            p2 += 1
            p += 1
        elif p2 == len2:
            array[p] = list1[p1]
            p1 += 1
            p += 1
        else:
            if list1[p1] <= list2[p2]:
                array[p] = list1[p1]
                p1 += 1
                p += 1
            else:
                array[p] = list2[p2]
            # list3.append(list2[p2])
                p2 += 1
                p += 1
    return array
l1 = [55,52,56, 904, 4, 920]
l2 = [53, 56, 518, 523, 73]
l1 = mergesort(l1)
l2 = mergesort(l2)
print(l1)
print(l2)

