# Problem: Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed_node = None

        while head:
            new_node = ListNode(head.val)
            new_node.next = reversed_node
            reversed_node = new_node
            head = head.next
        
        return reversed_node