# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Naive / brute force: Turn the linked list into an array and perform a two pointer algorithm on the list with l = 0, and r =  n-1. Increment both, creating a new linked list as you add l then r on each iteration. O(n) time but O(n) space.
        # proposed solution: See that the initial list and be seperated into two halves, with the second hald (half - end) being reversed. If these two lists merge, they produce the expected solution. step1: find the midpoint/half by using the slow and fast pointer appraoch. Then create two new linked list pointers which represent the left and right halves, reverse the second half before merging the two to get the solution: O(n) time and O(1) space due to only pointers being used/initialized

        # no dummy needed because head is guaranteed to be nonempty
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        prev = slow.next = None # initializes prev as None while cutting off first and second halves
        while second:
            tmp = second.next # temp holds second.next which is lost when you reverse
            second.next = prev
            prev = second
            second = tmp
        
        first, second = head, prev # prev gets the new start of the reversed list
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

        # time: O(n), space: O(1)
        