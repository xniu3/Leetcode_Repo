class Solution:
    from typing import List
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rowlen , collen = len(board) , len(board[0])
        
        results = [[0] * collen for _ in range(rowlen)]
        direct = [(-1 , -1),(-1, 0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        def dfs(x , y):
            if not 0 <= x < rowlen or not 0 <= y < collen:
                return
            liveheigh = 0
            for di in direct:
                newx , newy = x + di[0] , y + di[1]
                if 0<= newx < rowlen and 0 <= newy < collen and board[newx][newy]:
                    liveheigh += 1
            if liveheigh < 2 and board[x][y]:
                results[x][y] = 0
            elif (liveheigh == 2 or liveheigh == 3) and board[x][y]:
                results[x][y] = 1
            elif liveheigh > 3 and board[x][y]:
                results[x][y] = 0
            elif liveheigh == 3 and not board[x][y]:
                results[x][y] = 1
            else:
                results[x][y] = 0
        for i in range(rowlen):
            for j in range(collen):
                dfs(i,j)
        return results


if __name__ == '__main__':
    Solu = Solution()
    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    ret = Solu.gameOfLife(board)
    print(ret)