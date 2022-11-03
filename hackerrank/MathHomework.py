

def MathHomework(array , threshold):
    # n = len(array)
    select , noselect = 0 , 0
    minval = None
    if array[-1] - array[0] < threshold:
        return len(array)
    for index, value in enumerate(array):
        if index == 0:
            select, noselect = 1 , 1
            minval = value
        else:
            temp = noselect
            noselect = select
            select = min(select + 1, temp + 1)
            # print("select is ",select, "noselect is ",noselect)
            if value - minval >= threshold:
                break
        
    return select # if select <= noselect else noselect
def find_binary(points, low, high, key, ans):
    if(low<high):
        mid = (low + high)//2
        if(points[mid]==key):
            ans = mid
            return
        elif(points[mid]>=key):
            ans = min(ans,mid)
            find_binary(points, low, mid-1,key,ans)
        else:
            find_binary(points, mid+1, high, key, ans)
        
def minNum(threshold, points):
    if (threshold + points[0] > points[len(points)-1]):
        return len(points)
    key = threshold + points[0]
    ans = len(points)-1
    find_binary(points,0,len(points)-1,key,ans)
    ans = ans + 1
    
    _ans = (ans + 2)//2
    return _ans
print(minNum(402,[25,162,206,224,264,288,334,364,367,389,405,454,478,479,482,509,517,545,578,626,657,692,705,720,734,747]))
print(MathHomework([25,162,206,224,264,288,334,364,367,389,405,454,478,479,482,509,517,545,578,626,657,692,705,720,734,747],402))
'''
Failing two test cases

Threshold: 402
Points: 25,162,206,224,264,288,334,364,367,389,405,454,478,479,482,509,517,545,578,626,657,692,705,720,734,747
Output: 13
Expected: 10

One more hidden test case failed, Only output (51) was visible
'''