from typing import List
def getRow(rowIndex: int) -> List[int]:
    if rowIndex == 0:
        return [1]
    row1 , row2 = [1] * (rowIndex + 1) , [1] * (rowIndex + 1)
    # rowIndex = 4 
    #       1       1 1 1 1 
    #      1 1      1 1 1 1
    #     1 2 1     1 2 1 1
    #    1 3 3 1    1 3 3 1
    for i in range(rowIndex + 1):
        for j in range(i - 1):
            if i % 2 == 0:
                row2[j + 1] = row1[j + 1] + row1[j]
            else:
                row1[j + 1] = row2[j + 1] + row2[j]
        print("row1 is ", row1)
        print("row2 is ", row2)
    if rowIndex % 2 == 1:
        return row1
    else:
        return row2
ret = getRow(3)
print(ret)