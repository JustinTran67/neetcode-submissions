"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # brute force/naive appraoch: Create the copy as an array first, then turn that array back into a linked list.
        # proposed approach: To create a deep copy we need to have copies of both the next and random pointer, however, the random pointer can point to forward nodes that have not been created yet on the first pass. Sacrificing some memory to map the original nodes to the copies in a hashmap will allow us to reinitialize the random pointers in the new list. O(n), O(n)

        dummy = Node(0)
        node, tail = head, dummy
        lookup = {}

        while node:
            tail.next = Node(node.val, None, None)
            lookup[node] = tail.next # map every original node -> copy
            node = node.next
            tail = tail.next
        
        tail = dummy
        while head:
            if head.random:
                tail.next.random = lookup[head.random]
            head = head.next
            tail = tail.next
        
        return dummy.next

        # O(n), O(n)
            