class Node:
    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        #initlize dummy boundyes
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node: Node) -> None:
        nxt = node.next
        prev = node.prev
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node: Node):
        prev = self.right.prev
        self.right.prev = node
        node.prev = prev
        node.next = self.right
        prev.next  = node


    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value
        return -1 

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove(node)
            self.insert(node)
        else:
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.insert(new_node)

            if len(self.cache) > self.cap:
                lru = self.left.next
                self.remove(lru)
                del self.cache[lru.key]

        
