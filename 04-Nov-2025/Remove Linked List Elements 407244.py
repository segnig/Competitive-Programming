# Problem: Remove Linked List Elements - https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        prev_node = dummy
        current = head

        while current:

            while current and current.val == val:
                current = current.next
            
            prev_node.next = current
            prev_node = prev_node.next

            if current:
                current = current.next
        
        return dummy.next