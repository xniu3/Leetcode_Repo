def solution(centers):
    centers.sort()
    # help(centers.sort)
    # for center in centers:
    # print(centers)
    n = len(centers)
    ret = 0
    for i in range(n - 1):
        point1x , point1y = centers[i][0] , centers[i][1]
        for j in range(i + 1, n):
            point2x , point2y = centers[j][0] , centers[j][1] 
            if not 0 <= point2x - point1x <= 2:
                break
            else:
                if not -2 <= point2y - point1y <= 2:
                    continue
                else:
                    ret += 1
    return ret
            
    
