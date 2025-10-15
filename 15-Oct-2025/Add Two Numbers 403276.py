# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def get_val(node):
            return node.val if node else 0

        head = ListNode()
        temp = head
        carry = 0

        while l1 or l2:
            res = get_val(l1) + get_val (l2) + carry
            carry = res // 10
            res  %= 10
            temp.next = ListNode(val=res)
            temp = temp.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry:
            temp.next = ListNode(val=carry)
            temp = temp.next
        
        return head.next


