# Definition for singly-linked list.
# Time complexity: O(max(m, n)). m, n represents the length of l1 and l2 respectively.
# Space complexity: O(max(m, n)). Length of new linked list is at most max(m, n) + 1
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Declare the result as linked list
        result = ListNode()
        
        # the current node of the result list during loop
        ptr = result
        
        carry = 0
        
        # if l1 or l2 is not None or carry is not zero. 
        # if carry still nonzero after both list has ended, 
        # the loop will continue to add the remaining to digits to result List
        # add l1 + l2 to carry
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            
            # if sum is greater than 9, only add the last digit 
            # to the list and carry the remaining part to next loop
            # %10 = modulus with 10
            # put current carry%10 value in linked-list
            ptr.next = ListNode(carry%10)
            
            # next linked list
            ptr = ptr.next
            
            # floor division (clear carry)
            carry //= 10
        
        return result.next # if not .next, first element will be irrelated zero
        