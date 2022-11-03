
def dataUpdates(array, updates):
    length = len(array)
    signal = [1] * length
    for update in updates:
        for i in range(update[0]-1,update[1]):
            signal[i] *= -1
    for i in range(length):
        array[i] *= signal[i]
    return array

print(dataUpdates([1,-4,-5,2], [[2,4],[1,2]]))