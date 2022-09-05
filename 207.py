from typing import List
def canFinish( numCourses: int, prerequisites: List[List[int]]) -> bool:
    from collections import defaultdict , deque
    edges = defaultdict(list)
    visited = [0] * numCourses
    for i in range(numCourses):
        edges[i] = list()
    for pre in prerequisites:
        source , target = pre[1], pre[0]
        edges[source].append(target)
    print("edges is ",edges)
    for i in range(numCourses):
        stack = deque()
        stack.append(i)
        visited[i] = 1
        while stack:
            print("stack is ",stack)
            nextnode = stack.popleft()
            print("nextnode is ",nextnode)
            if visited[nextnode] == 1:
                return False
            visited[nextnode] = 1
            nodelist = edges[nextnode]
            print("nextlist is ",nodelist)
            for node in nodelist:
                if visited[node] == 1:
                    return False
                else:
                    stack.append(nextnode)
        visited[i] = 2
    return True
a = 3
b = [[0,1],[0,2],[1,0]]

ret = canFinish(a,b)
print(ret)