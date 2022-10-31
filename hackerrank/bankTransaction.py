def bankTransaction(transactions):
    from heapq import heappush, heappop , heapify
    minHeap = list()
    heapify(minHeap)
    bank = 0
    count = 0
    for index, num in enumerate(transactions):
        bank += num
        if bank > 0 and bank > 10e9 + 7:
            bank = bank % (10e9 + 7)
        if transactions[index] < 0:
            minHeap.append(num)
        if bank < 0:
            bank -= num
            count += 1
    return len(transactions) - count

trans = [3,2,-5,-6, -1,4]
print(bankTransaction(trans))
trans2 = [3, 2, -5, -1, -3, 3, -2]
print(bankTransaction(trans2))
