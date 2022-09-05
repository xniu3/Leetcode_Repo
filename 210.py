from typing import List
def findOrder(prerequisites: List[List[int]]) -> List[int]:
    from collections import defaultdict
    edges = defaultdict(list)
    def addedge(course):
        source , target = course[1] , course[0]
        edges[source].append(target)
    for course in prerequisites:
        addedge(course)
    print("edges is",edges)
if __name__ == '__main__':
    ret = [[1,0],[2,0],[3,1],[3,2]]
    findOrder(ret)