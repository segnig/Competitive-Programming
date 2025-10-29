# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_nodes = {}

    def _delete(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _insert(self, node):
        last_node = self.tail.prev
        last_node.next = node
        node.prev = last_node
        node.next = self.tail
        self.tail.prev = node
        return node

    def get(self, key: int) -> int:
        if key in self.key_nodes:
            node = self.key_nodes[key]
            self._delete(node)
            self._insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_nodes:
            node = self.key_nodes[key]
            node.val = value
            self._delete(node)
            self._insert(node)
        else:
            if len(self.key_nodes) == self.capacity:
                lru_node = self.head.next
                self._delete(lru_node)
                del self.key_nodes[lru_node.key]
            
            new_node = Node(key, value)
            self._insert(new_node)
            self.key_nodes[key] = new_node    


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)