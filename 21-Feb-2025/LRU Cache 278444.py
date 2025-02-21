# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.maps = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        self.capacity = capacity

    def add_node(self, node):
        node_prev, node_next = self.left, self.left.next
        node_prev.next = node
        node_next.prev = node
        node.next = node_next
        node.prev = node_prev
    def remove_node(self, node):
        node_next, node_prev = node.next, node.prev
        node_prev.next = node_next
        node_next.prev = node_prev
    def get(self, key: int) -> int:
        if key in self.maps:
            node = self.maps[key]
            self.remove_node(node)
            self.add_node(node)
            return node.val
        
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.maps:
            node = self.maps[key]
            node.val = value
            self.remove_node(node)
            self.add_node(node)
        
        else:
            node = Node(key, value)
            if len(self.maps) >= self.capacity:
                removed_node = self.right.prev
                self.remove_node(removed_node)
                del self.maps[removed_node.key]

            self.add_node(node)
            self.maps[key] = node

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)