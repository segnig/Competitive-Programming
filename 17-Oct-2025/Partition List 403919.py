# Problem: Partition List - https://leetcode.com/problems/partition-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        less_than_x = ListNode()
        greater_or_equal_x = ListNode()

        less, great = less_than_x, greater_or_equal_x

        while head:
            if head.val < x:
                less.next = ListNode(head.val)
                less = less.next
            else:
                great.next = ListNode(head.val)
                great = great.next
            
            head = head.next
        
        result = less_than_x
        less.next = greater_or_equal_x.next

        return result.next

        
        