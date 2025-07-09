# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode()
        tail=head
        firstNode,secondNode=list1,list2
        while firstNode and  secondNode :
            if firstNode.val<secondNode.val:
                tail.next=firstNode
                firstNode=firstNode.next
            else:
                tail.next=secondNode
                secondNode = secondNode.next
            tail=tail.next
        
        tail.next=firstNode if firstNode else secondNode


        return head.next
        