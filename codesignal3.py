def solution(matrix, queries):
    from heapq import heappush, heappop, heapify
    white , black = list() , list()
    whitestack , blackstack = list() , list() 
    m , n = len(matrix) , len(matrix[0])
    for i in range(m):
        for j in range(n):
            if (i + j) % 2 == 0:
                white.append([matrix[i][j], i , j ])
            else:
                black.append([matrix[i][j], i , j ])
    
    heapify(white)
    heapify(black)
    for query in queries:
        whitetime , blacktime = query[1] , query[0]
        for i in range(whitetime + 1):
            #print("white is ",white)
            whitestack.append(heappop(white))
        for j in range(blacktime + 1):
            blackstack.append(heappop(black))
        print("whitestack is",whitestack)
        print("blackstack is ",blackstack)
        print("vals are",whitestack[-1][0] , blackstack[-1][0])
        summer = whitestack[-1][0] + blackstack[-1][0]
        if summer % 2 == 0:
            whitestack[-1][0] = blackstack[-1][0] =  summer // 2
        else:
            if whitestack[-1][0] > blackstack[-1][0]:
                whitestack[-1][0] = summer // 2 + 1
                blackstack[-1][0] = summer // 2 
            else:
                
                whitestack[-1][0] = summer // 2
                blackstack[-1][0] = summer // 2 + 1
        for i in range(whitetime + 1):
            temp = whitestack.pop()
            print("popped white are",temp)
            heappush(white, temp)
        for j in range(blacktime + 1):
            temp = blackstack.pop()
            print("popped black are",temp)
            heappush(black, temp)
    for k in range(len(white)):
        matrix[white[k][1]][white[k][2]] = white[k][0]
    for k in range(len(black)):
        matrix[black[k][1]][black[k][2]] = black[k][0]
    return matrix
if __name__ == '__main__':

    solu = solution(matrix = [[2, 0, 4],
          [2, 8, 5],
          [6, 0, 9],
          [2, 7, 10],
          [4, 3, 4]], queries = [[0, 0], [1, 3]])
    print(solu)
    