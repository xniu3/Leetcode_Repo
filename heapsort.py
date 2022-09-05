''''''
def heapify(arr,root,end):
    while True:
        child = 2 * root + 1
        if child >= end:
            break
        while child + 1 < end and arr[child] <= arr[child + 1]:
            child += 1
        if arr[root] <= arr[child]:
            arr[root], arr[child] = arr[child] , arr[root]
            root = child
        else:
            break

def heapsort(arr):
    n = len(arr)
    first_root = n // 2 - 1
    for root in range(first_root,-1,-1):
        heapify(arr,root,n - 1)
    for end in range(n - 1, -1 ,-1):
        arr[0], arr[end] = arr[end] ,arr[0]
        heapify(arr,0,end)

if __name__ == "__main__":
    # from heapq import heapify
    arr = [3,9,4,0,5,2,7,8,6]
    heapsort(arr)

    print(arr)
