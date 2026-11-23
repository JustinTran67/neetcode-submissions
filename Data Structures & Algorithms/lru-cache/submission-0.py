# brute force appraoch: store all key value pairs in an array to get the LRU at the left of the array and the most recently used at the right. O(n) time operations for almost all functions
# proposed appraoch: Use a doubly linked list + hashmap to store the key value pairs and optomize space and time complexity to O(1), O(n) total. Functions like get and put will run in O(1) time using this appraoch because only insterting/removing elements from the hashmap and doubly linked list happen which all run O(1) time. We can define the linked ist Node class and helper functions for intert and delete to simplify our code.

class Node:
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # key -> node(key, val)
        self.left, self.right = Node(), Node() # left and right dummies that allow us to access and edit LRU and MRU
        self.left.next, self.right.prev = self.right, self.left # connect the dummies
    
    # inserts at the right MRU
    def insert(self, node):
        prv, nxt = self.right.prev, self.right
        prv.next = nxt.prev = node
        node.next, node.prev = nxt, prv

    # removes node at key
    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key]) # make it the MRU
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.left.next
            del self.cache[lru.key] # remove LRU from hashmap
            self.remove(lru) # remove LRU from doubly linked list
        
