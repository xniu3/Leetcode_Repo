def mergesort(array):

    if not array:
        return array
    if len(array) > 1:
        mid = len(array) // 2
        # print("mid is ",array[:mid],array[mid:])
        left = mergesort(array[:mid])
        right = mergesort(array[mid:])
        l1 , l2 = len(left) , len(right)
        p1 , p2 = 0 , 0
        parray = 0
        while p1 < l1 or p2 < l2:
            if p1 == l1:
                array[parray] = right[p2]
                p2 += 1
                parray += 1
            elif p2 == l2:
                array[parray] = left[p1]
                p1 += 1
                parray += 1
            else:
                if left[p1] < right[p2]:
                    array[parray] = left[p1]
                    p1 += 1
                    parray += 1
                else:
                    array[parray] = right[p2]
                    p2 += 1
                    parray += 1
        return array
    else:
        return array

def heapify(array, root, end):
    while True:
        child =  2 * root + 1
        if child >= end:
            break
        while child + 1 < end and array[child] < array[child + 1]:
            child += 1
        if array[root] < array[child]:
            array[root] , array[child] = array[child] , array[root]
            root = child
        else:
            break

def heapsort(array):
    n = len(array)
    first_root = n // 2 - 1
    print("first root is ", first_root)
    for root in range(first_root , -1, -1):
        heapify(array, root, n - 1)
    print("array is now (after first root)", array)
    for end in range(n - 1, -1, -1):
        array[0] , array[end] = array[end] , array[0]
        heapify(array, 0, end)
    print("array is now", array)

def qsort(arr, start, end):
    if start > end: 
        return
    def partition(arr, start, end):
        pivot = arr[start]
        i = start + 1
        while i <= end:
            if pivot < arr[i]:
                arr[i], arr[end] = arr[end], arr[i]
                end -= 1
            else:
                i += 1
        if end > start:
            arr[start], arr[end] = arr[end], arr[start]
        return end
    mid = partition(arr, start, end)
    qsort(arr, start, mid-1)
    qsort(arr, mid+1, end)
array = [7,55,52,56, 918, 2, 920, 900, 4, ]
heapsort(array)
print(array)


