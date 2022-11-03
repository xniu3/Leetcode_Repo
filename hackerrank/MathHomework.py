

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
            if value - minval >= threshold:
                break
    return select if select <= noselect else noselect

print(MathHomework([1,2,3,5,8],7))
