from heapq import heapify, heappush, heappop
from typing import List
class Solution:
    
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        fuel = startFuel
        if fuel >= target:
            return 0
        prev_loc = 0        
        h = list()
        fuelcount = 0
        n = len(stations)
        for i in range(n + 1):
            loc = stations[i][0] if i < n else target
            fuel -= loc - prev_loc
            while fuel < 0 and h:
                fuel += (-heappop(h))
                fuelcount += 1
            if fuel < 0:
                return -1
            if i < n:
                heappush(h, -stations[i][1])
                prev_loc = loc
        return fuelcount
