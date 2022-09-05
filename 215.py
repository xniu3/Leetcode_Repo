class Solution:
    def findKthLargest(self, nums,k) -> int:
        def heapify(arr, root, end):
            
            while True:
                child = 2 * root + 1
                if child > end:
                    break
                if child + 1 <= end and arr[child] > arr[child + 1]:
                    child += 1
                if arr[root] > arr[child]:
                    arr[root] , arr[child] = arr[child] , arr[root]
                    root = child
                else:
                    break
        def heapsort(arr):
            length = len(arr)
            first_root = length // 2 -1
            for root in range(first_root, -1 , -1):
                heapify(arr, root, length - 1)
            print("this time arr is ",arr)
            second_root = length 
            for end in range(second_root -1  , -1 , -1):
                nums[0] , nums[end] = nums[end] , nums[0]
                heapify(arr , 0 , end -1 )
            print("this time arr is ",arr)
        heapsort(nums)
        return nums[k]
if __name__ == '__main__':
    Solu = Solution()
    nums = [3,2,3,1,2,4,5,5,6]
    ret = Solu.findKthLargest(nums,2)
    print(ret)