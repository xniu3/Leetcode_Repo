


if __name__ == '__main__':
    nums = [1,2,3,4]
    hashtable = dict()
    length = len(nums)
    for i in range(length // 2):
        hashtable[nums[i * 2]] = nums[i * 2 + 1]
    print(hashtable) 