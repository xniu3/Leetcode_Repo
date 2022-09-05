matrix = [[1,5,9],[10,11,13],[12,13,15]]
rowlen , collen = len(matrix) , len(matrix[0])
n = rowlen
8

def findnum(num):
    x , y = n - 1 , 0
    total = 0
    while x >= 0:
        y = 0
        while y < collen and matrix[x][y] <= num:
            y += 1
        total += y
        x -= 1
    return total
print(findnum(8))
