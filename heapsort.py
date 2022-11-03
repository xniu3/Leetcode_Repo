def heapify(arr:list, root, end):
    while True:
        child = 2 * root + 1
        if child >= end:
            break
        while child + 1 < end and arr[child ] <= arr[child + 1]:
            child += 1
        if arr[root] <= arr[child]:
            arr[root] , arr[child] = arr[child] , arr[root]
            root = child
        else:
            break

def heapsort(arr):
    n = len(arr)
    first_root = n // 2 - 1
    print("0th arr is ",arr)
    for root in range(first_root,-1, -1):
        heapify(arr,root, n - 1)
    print("1st arr is ",arr)
    for end in range(n - 1, -1, -1):
        arr[0] , arr[end] = arr[end] , arr[0]
        heapify(arr, 0 ,end)
    print("2nd arr is ",arr)
arr = [4, 7, 2, 52, 55, 920, 900]
heapsort(arr)
print(arr)
