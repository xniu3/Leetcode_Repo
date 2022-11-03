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
def bankTransaction1(transactions):
    from heapq import heappush, heappop, heapify
    h = list()
    balance = 0
    n = len(transactions)
    # print("n is ",n)
    transcount = 0
    for i in range(n):
        # print("transaction value is ",transactions[i])
        if transactions[i] >= 0 or i == n - 1:
            while h:
                min_amount = heappop(h)
                # print("min amount is ",min_amount)
                if balance >= min_amount:
                    balance -= min_amount
                    transcount += 1
                else:
                    break
            h = list()
            balance += transactions[i]
            transcount += 1
        else:
            heappush(h, -transactions[i])
    return transcount
trans = [3,2,-5,-6, -1,4]
print(bankTransaction1(trans))
trans2 = [3, 2, -5, -1, -3, 3, -2]
print(bankTransaction1(trans2))
trans3 = [10, -10, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ]
print(bankTransaction1(trans3))
