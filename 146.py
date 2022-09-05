

class DualListNode:
    def __init__(self, key = 0 , value = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class LRUCache:
    def __init__(self,capacity:int):
        self.cache = dict()
        self.head = DualListNode()
        self.tail = DualListNode()
        self.head.next = self.tail
        self.tail.next = self.head
        self.capacity = capacity
        self.size = 0
    def add_to_head(self,node:DualListNode):
        # node.prev = self.head
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    def remove_node(self,node:DualListNode):
        node.prev.next = node.next
        node.next.prev = node.prev
    def move_to_head(self,node:DualListNode):
        self.remove_node(node)
        self.add_to_head(node)
    def remove_tail(self): # ,node:DualListNode):
        node = self.tail.prev
        self.remove_node(node)
        return Node
        

    def get(self, key:int):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.move_to_head(node)
        return node.value
    def put(self,key:int,value:int):
        if key not in self.cache:
            node = DualListNode(key , value)
            self.cache[key] = value
            self.add_to_head(node)
            self.size += 1
            if self.size > self.capacity:
                removed = self.remove_tail()
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            node = self.cache[key]
            node.value = value