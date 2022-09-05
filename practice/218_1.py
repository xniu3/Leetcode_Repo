class Solution:
    def getSkyline(self, buildings):
        from heapq import heappush , heappop, heapify
        from sortedcontainers import SortedDict , SortedList
        
        skyline = SortedDict()
        skyline[0] = 1
        stack = list()
        ret = list()
        for build in buildings:
            left , right , height = build[0] , build[1] , build[2]
            heappush(stack , (left, -height))
            heappush(stack , (right, height))
        print("stack is ",stack)
        while stack:
            x, h = heappop(stack)
            print("popped x and h is ",x,h)
            print("old skyline is ",skyline)
            print("old ret is ",ret)
            if h < 0:
                if h in skyline:
                    skyline[h] += 1
                else:
                    skyline[h] = 1
                    if h == skyline.keys()[0]:
                        ret.append([x,-h])

            else:
                skyline[-h] -= 1
                if not skyline[-h]:
                    
                    skyline.pop(-h)
                    if -skyline.keys()[0] < h:
                        ret.append([x,-skyline.keys()[0]])
            print("new skyline is ",skyline)
            print("new ret is ",ret)
        return ret
    def offer2(self,n:int):
        numof2 = 0
        while n % 2 == 0:
            n = n // 2
            numof2 += 1
        return numof2
if __name__ == '__main__':
    Solu = Solution()
    #array = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    array = 9
    ret = Solu.offer2(array)
    print(ret)

            