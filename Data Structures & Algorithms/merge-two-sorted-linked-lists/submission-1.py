# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # naive/brute force: Place all values from the lists into an array and sort the array and turn it back into a linked list. O(nlogn) for sorting
        # Proposed solution: traverse through both linked lists, comparing the nodes to each other in each and always placing the smallest value first. Use a dummy node as teh "start" to allow you to start the list. Have a tail node which will be what actually appends the next pointer in the linked list. Return what is left. The fummy allows us to grab the head instantly. Should be an O(n + m) solution

        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        # handle remaining if one runs out of nodes first or is initially empty
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        return dummy.next

        # time complexity: O(n + m) n = # of nodes in list1, m = # of nodes in list2, space complexity: O(1)
            