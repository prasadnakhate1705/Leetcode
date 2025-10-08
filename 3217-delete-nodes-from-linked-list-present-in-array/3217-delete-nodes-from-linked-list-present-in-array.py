# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        
        nums_set = set(nums)
        
        node = head
        prev = None

        while node:
            if node.val in nums_set:
                if prev is None:
                    head=head.next
                    node=head
                    continue
                
                prev.next=node.next
            else:
                prev=node
                
            node=node.next
        
        return head