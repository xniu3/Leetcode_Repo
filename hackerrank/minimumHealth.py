from heapq import heappush , heappop, heapify
def minimumHealth(initial_players:list, new_players:list, rank:int):
    def findtopk(temp,rank):
        array = temp[:]
        print("array is ",array)
        ret = 0
        heapify(array)
        for i in range(rank):
            ret = heappop(array)
            print("popped value  is ",ret)
        return ret
    ret = list()
    initial_length = len(initial_players)
    new_length = len(new_players)
    enemies = [-i for i in initial_players]
    value = findtopk(enemies,rank)
    ret.append( -value)
    for i in range(new_length):
        enemies.append(-new_players[i])
        print("enemies is ",enemies)
        value = findtopk(enemies,rank)
        ret.append( -value)
    return ret
print(minimumHealth([1,2],[3,4],2))
    # initial [1,2] new player [3,4]
