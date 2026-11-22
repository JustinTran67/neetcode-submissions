# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # naive solution: turn the linked list into an array and return true if a duplicate element is found. O(n) time but O(n) memory. We can do better
        # Proposed solution: Use a fast and slow pointer, slow pointer will move one at a time, pointer.next, and the fast pointer will move 2 steps at a time, pointer.next.next. If a cycle exists, fast will eventually loop back and reach slow again -> return true, else return false. O(n) time and O(1) space

        slow, fast = head, head

        while fast and fast.next: # Move first because since slow and fast start at head, checking first will always return True
            slow = slow.next # move 1 step
            fast = fast.next.next # move 2 steps
            if slow == fast:
                return True
        
        return False

        # time: O(n), space: O(1)