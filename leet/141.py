# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head 
        seen = {}

        while current != None :
            seen[current] = seen.get(current , 0) + 1

            if seen.get(current) > 1 :
                return True
            
            current = current.next
        
        return False

        
# use set 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        seen = set()

        while current != None :
            if current in seen:
                return True
            
            seen.append(current)
            current = current.next
        

        return False