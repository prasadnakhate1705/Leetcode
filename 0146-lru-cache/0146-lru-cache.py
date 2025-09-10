class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.nxt = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.hash_map = {}
        self.size = 0
        self.capacity = capacity
    
    def remove(self, node):
        if node.prev:
            node.prev.nxt = node.nxt
        else:
            self.head = node.nxt
        
        if node.nxt:
            node.nxt.prev = node.prev
        else:
            self.tail = node.prev
            
        del self.hash_map[node.key]
        self.size -= 1
        
    def add(self,node):
        if self.head is None:
            self.head = self.tail = node
        else:
            self.head.prev = node
            node.nxt = self.head
            self.head = node
        self.hash_map[node.key] = node
        self.size += 1

    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1
        
        node = self.hash_map[key]
        
        # Only move the node if it's not already the head
        if node != self.head:
            self.remove(node)
            self.add(node)
        
        return node.value
    
    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            node = self.hash_map[key]
            node.value = value
            # Move the updated node to the head if it's not already there
            if self.head != node:
                self.remove(node)
                self.add(node)
        else:
            if self.size == self.capacity:
                if self.tail:
                    old_tail = self.tail
                    del self.hash_map[old_tail.key]
                    
                    if self.head == self.tail:
                        self.head = self.tail = None
                    else:
                        self.tail = old_tail.prev
                        # Crucial fix: unlink the old tail
                        self.tail.nxt = None
                        
                    self.size -= 1
            
            node = Node(key, value)
            self.add(node)