from collections import defaultdict

def DeliveryManagementSystem(cityNodes:int, cityFrom:list, cityTo:list, company:int):
    # n is the lengtn of list cityFrom and cityTo, which could be emitted when we do this practice 
    from collections import defaultdict,deque
    edges = defaultdict(list)

    n = len(cityFrom)
    ret = list()
    
    for i in range(n):
        source , target = cityFrom[i] , cityTo[i]
        edges[source].append(target)
    print("edges is",edges)
    visited = [False] * (cityNodes + 1)
    print("visited is",visited)
    def dfs(node):
        print("the node is ",node)
        if visited[node]:
            return 
        ret.append(node)
        for nextnode in edges[node]:
            dfs(nextnode)
    dfs(company)
    bfsret = list()
    bfsvisited = [False] * (cityNodes + 1)
    def bfs(node):
        nonlocal bfsret
        queue = deque()
        print("the node is ",node)
        if visited[node]:
            return
        queue.append(node)
        while queue:
            curr = queue.popleft()
            if not bfsvisited[curr] and curr != company:
                bfsret.append(curr)
            bfsvisited[curr] = True
            for nextnode in edges[curr]:
                queue.append(nextnode)
        return bfsret
    bfs(company)
    return bfsret
    # return ret
    # print(edges)
res = DeliveryManagementSystem(5,[1,2,2,],[2,3,4,],1)
res = DeliveryManagementSystem(5,[1,1,2,3,1,],[2,3,4,5,5],1)
print("res is ",res)

