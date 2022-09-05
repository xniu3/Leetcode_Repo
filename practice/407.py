class Solution:
    def trapRainWater(self, heightMap) -> int:
        from heapq import heapify , heappush , heappop
        
        row , col = len(heightMap) , len(heightMap[0])
        if row <= 2 or col <= 2:
            return 0
        stack = list()
        visited = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if i == 0 or i == row - 1 or j == 0 or j == col - 1:
                    visited[i][j] = 1
                    newarray = [  heightMap[i][j] , i,j   ]
                    heappush(stack, newarray )
        
        ret = 0
        directions = [(0, 1) , (0, -1),(1, 0) , (-1, 0)]
        
        
        while stack:
            # print("stack is ",stack)
            oldarray = heappop(stack)
            height ,x , y  = oldarray[0] , oldarray[1] , oldarray[2]
            for di in directions:
                nx , ny = x + di[0] , y + di[1]
                if 0<= nx < row and 0<= ny < col and not visited[nx][ny]:
                    if height > heightMap[nx][ny]:
                        temp_adder = height - heightMap[nx][ny]
                        ret += temp_adder
                        print("ret added value of ",temp_adder)
                    visited[nx][ny] = 1
                    newarray = [ max(height ,heightMap[nx][ny]), nx, ny]
                    heappush(stack, newarray)
        return ret
    def trapRainWater2(self, heightMap) -> int:
        from heapq import heapify , heappush , heappop
        
        row , col = len(heightMap) , len(heightMap[0])
        if row <= 2 or col <= 2:
            return 0
        stack = list()
        visited = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if i == 0 or i == row - 1 or j == 0 or j == col - 1:
                    visited[i][j] = 1
                    newarray = [  i,j ,  heightMap[i][j] ]
                    heappush(stack, newarray )
        
        ret = 0
        directions = [(0, 1) , (0, -1),(1, 0) , (-1, 0)]
        
        
        while stack:
            # print("stack2 is", stack)
            oldarray = heappop(stack)
            x , y , height = oldarray[0] , oldarray[1] , oldarray[2]
            for di in directions:
                nx , ny = x + di[0] , y + di[1]
                if 0<= nx < row and 0<= ny < col and not visited[nx][ny]:
                    if height > heightMap[nx][ny]:
                        temp_adder = height - heightMap[nx][ny]
                        ret += temp_adder
                        print("2 ret added value of ",temp_adder)
                    visited[nx][ny] = 1
                    newarray = [  nx, ny , max(height , heightMap[nx][ny])]
                    heappush(stack, newarray)
        return ret
if __name__ == "__main__":
    Solu = Solution()
    heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
    ret = Solu.trapRainWater(heightMap)
    ret2 = Solu.trapRainWater2(heightMap)
    print(ret)
    print(ret2)