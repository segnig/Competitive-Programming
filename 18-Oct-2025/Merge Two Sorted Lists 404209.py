# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = dummy = ListNode()
        
        while list1 and list2:
            node = ListNode()
            if list1.val >= list2.val:
                node.val = list2.val
                temp.next = node
                list2 = list2.next
            else:
                node.val = list1.val
                temp.next = node
                list1 = list1.next
            temp = temp.next
        
        # if there are elements left 
        if list1:
            temp.next = list1
        else:
            temp.next = list2
            
        return dummy.next
        
                
                
        