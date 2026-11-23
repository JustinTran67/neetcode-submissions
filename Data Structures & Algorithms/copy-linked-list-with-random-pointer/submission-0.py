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
        # proposed approach: Iterate through the original array. Creating a new node for each node traversed through. Have a dummy and a tail, dummy allows for us to return the head and handle a potential empty list. Tail is what we use to move through the new copy while creating new nodes. O(n) time, O(1) space

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
            