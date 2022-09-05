class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rowlen , collen = len(grid) , len(grid[0])
        visited = [[0] * collen for _ in range(rowlen)]
        island_list = list()
        max_area = 0
        def bfs(x,y,island):
            nonlocal max_area
            if not 0<= x < rowlen or not 0 <= y < collen:
                return False
            if visited[x][y]:
                return False
            visited[x][y] = 1
            island += 1
            max_area = max_area if max_area > island else island 
            direct = [(0,1),(0,-1),(1,0),(-1,0)]
            for di in direct:
                newx , newy = x + di[0] , y + di[1]
                bfs(newx , newy , island)
        for i in range(rowlen):
            for j in range(collen):
                if grid[i][j] and not visited[i][j]:
                    bfs(i,j,0)
        return max_area