# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        left = l1
        right = l2
        result_head = ListNode(0, None)
        result = result_head
        while left or right:
            sum = carry
            if left:
                sum += left.val
            if right:
                sum += right.val
            
            if sum >= 10:
                sum -= 10
                carry = 1
            else:
                carry = 0
            
            result.val = sum
                        
            if left:
                left = left.next
            if right:
                right = right.next
            
            if left or right or carry:
                result.next = ListNode(carry, None)
                result = result.next

        return result_head
