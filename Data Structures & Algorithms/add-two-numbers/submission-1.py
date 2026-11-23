# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # naive/brute force solution: turn the lists into integers or into lists then into integers and add them normally through arithmetic operations. Then turn the number back into a linked list after turning it into digits in a list. Can be O(n) time but O(n) space.
        # Proposed solution: build a new list adding new nodes with the value = the sum of the values of both nodes. To handle > 1 digit sums, have a saved variable to carry the front value of the sum to carry over to sum with the next node or as a new node. Questions: Should I be returning the head of the new linked list or the sum as an integer? Is it possible for one or both of the linked lists to be empty? Just to confirm each node can be a single digit from 0-9 correct? Can l1 and l2 be different lengths?
        # remove last digit (//10), get last digit (%10)

        dummy = ListNode() # starts the new list and allows us to grab the start
        tail, carry = dummy, 0 # what we move along + carry over integer

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            carry = carry + val1 + val2
            tail.next = ListNode(carry % 10)
            carry = carry // 10
            l1, l2, tail = l1.next if l1 else None, l2.next if l2 else None, tail.next # increment to next
        
        return dummy.next

        # O(n) time, O(1) space. n is length of longest list (l1 or l2 or both same length)
        

