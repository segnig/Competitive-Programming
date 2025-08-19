# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        queue = [(head.val, i) for i, head in enumerate(lists) if head]
        
        heapify(queue)

        result = ListNode()
        temp = result

        while queue:
            val, index = heappop(queue)
            node = lists[index]
            temp.next = ListNode(node.val)
            if node.next:
                heappush(queue, (node.next.val, index))
            if node.next:
                lists[index] = node.next
            else:
                lists[index] = None

            temp = temp.next
        return result.next