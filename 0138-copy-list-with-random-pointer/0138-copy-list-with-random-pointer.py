"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        new_head = None
        dummy = head
        prev = None
        Nodes_dict = {}

        ## Next Link
        while dummy!= None:
            if new_head is None:
                node = Node(head.val)
                Nodes_dict[head]=node
                new_head = node
                prev = node
                dummy=dummy.next
                continue
            
            node = Node(dummy.val)
            Nodes_dict[dummy]=node
            prev.next = node
            prev=prev.next
            dummy=dummy.next
        

        # Random  Link
        dummy = head
        while dummy!= None:
            node = Nodes_dict[dummy]
            if dummy.random:
                node.random = Nodes_dict[dummy.random]
            else:
                node.random = None
            dummy=dummy.next 

        return new_head