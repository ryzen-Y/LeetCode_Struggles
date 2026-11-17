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
        dummy = Node(0)
        tail = dummy 

        curr = head 
        info = {}

        while curr != None :
            new_node = Node(curr.val)
            info[curr] = new_node
            tail.next = new_node
            tail = tail.next

            curr = curr.next

        tail = dummy.next
        curr = head 

        while curr  != None :
            tail.random = info.get(curr.random)
            tail = tail.next
            curr = curr.next
        
        return dummy.next

        