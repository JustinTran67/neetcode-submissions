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

        lookup = {None: None}

        curr = head
        while curr:
            copy = Node(curr.val)
            lookup[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = lookup[curr]
            copy.next = lookup[curr.next]
            copy.random = lookup[curr.random]
            curr = curr.next
        
        return lookup[head]

        # O(n), O(n)
            