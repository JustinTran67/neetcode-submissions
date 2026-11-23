# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Clarifying questions for interviewer: Can n ever be greater than the size of the list? Can the list be empty, if so will n be 0? What should an empty list return?
        # Brute force, naive solution: turn the linked list into an array and then remove the nth node from the array and turn it back into a linked list: O(n) time but O(n) space.
        # Propsoed solution: to minimize space to O(1) we can use a two pointer appraoch with a fixed gap. Say n = 2, we can create two pointers left = head and right = head.next for i <= n. That way once right goes out of bounds, we will know the node to remove from the linked list with left. We can set a prev pointer to be behind left at all times to re attatch the next node to the list.

        prev, left, right = None, head, head
        for _ in range(n):
            right = right.next
        while right:
            prev = left
            left, right = left.next, right.next
        
        if prev and left.next:
            prev.next = left.next
            return head
        elif prev:
            prev.next = None
            return head
        elif left.next:
            return left.next
        return None

        # time complexity: O(n), space complexity: O(1)