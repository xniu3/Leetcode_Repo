def process(n:int,count:int):
    if count > 20:
        return 
    if n == 1:
        return n
    else:
        newnum = 0
        while n > 0:
            temp = n % 10
            newnum += temp ** 2
            n //= 10
        print("newnum is ",newnum + n ** 2)
        return process(newnum + n ** 2,count + 1)
def getroot(n):
    slow , fast = 1 , n // 2
    while slow <= fast:
        mid = (slow + fast) // 2
        if mid ** 2 == n:
            return mid
        elif mid ** 2 < n:
            slow = mid + 1
        else:
            fast = mid - 1
    return fast
# print(process(9,0))
def prime(self,n):
    for i in range(2 , int(n ** 0.5),1):
        if n % i == 0:
            return False
    return False
print(getroot(99))