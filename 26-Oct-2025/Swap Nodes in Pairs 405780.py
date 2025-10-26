# Problem: Swap Nodes in Pairs - https://leetcode.com/problems/swap-nodes-in-pairs/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #  head and head.next val not None that means we need to swap
        if not head or not head.next:
            return head

        # dummy node for simple 
        dummy = ListNode()
        dummy.next = head

        # have pointer for prev, first, second
        prev_node = dummy
        first_node = head
        second_node = head.next

        while first_node and second_node:

            first_node.next = second_node.next
            prev_node.next =  second_node
            second_node.next = first_node

            prev_node = first_node
            first_node = first_node.next

            if first_node:
                second_node = first_node.next
            else:
                second_node = None
        
        return dummy.next

