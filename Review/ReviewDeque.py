from collections import deque
def appender():
    # from collections import deque
    queue = deque()
    queue.append("Northgate")
    queue.appendleft("Eaux Claires")
    print("queue is ",queue)
    queue.append("Downtown")
    queue.append("Downtown")
    print("queue is ",queue, "has",queue.count("Downtown"),"Downtown")
    print("queue is ",queue, "has",queue.count("Southgate"),"Southgate")
    queue7 = deque()
    queue7.append("Downtown")
    queue7.append("Jasper Place")
    queue.extend(queue7)
    print("queue is ",queue, "has",queue.count("Downtown"),"Downtown")
    list103 = ["Castle Downs", "Eaux Claires"]
    queue.extendleft(list103)
    print("queue is ",queue, "has",queue.count("Eaux Claires"),"Eaux CLaires")
    dict51 = {"Castle Downs":51}
    set51 = set()
    set51.add("University")
    queue.extendleft(dict51)
    queue.extendleft(set51)
    list726 = ["University", "Belgravia","University"]
    queue.extendleft(tuple(list726))
    print("queue is ",queue, "has",queue.count("Castle Downs"),"Castle Downs")
    return queue
aqueue = appender()

print("---------------Index, Insert, Pop and Remove Part ------------")
def index_insert_pop_remove(queue:deque):
    
    print("University index is ",queue.index("University"))
    # print("Southgate index is ",queue.index("Southgate"))
    # Southgate not in the queue yet. 
    queue.pop()
    queue.popleft()
    print("University index is ",queue.index("University"))
    print("Eaux Claires index is ",queue.index("Eaux Claires"))
    queue.remove("Eaux Claires")
    print("Eaux Claires index is ",queue.index("Eaux Claires"))
    print("Queue is ",queue, "Belgravia",queue.index("Belgravia"))
    queue.reverse()
    print("Queue is ",queue, "Belgravia",queue.index("Belgravia"))
    queue.rotate(-4)
    print("Queue is ",queue, "Belgravia",queue.index("Belgravia"))
    queue.rotate(2)
    print("Queue is ",queue, "Belgravia",queue.index("Belgravia"))
index_insert_pop_remove(aqueue)
