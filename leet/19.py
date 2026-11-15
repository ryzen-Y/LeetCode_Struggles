# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def size (self , head):
        current = head
        count = 0 

        while current != None:
            count += 1
            current =  current.next
        return count 
        
        def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
            length = self.size(head)
            pos = length + 1 - n 

            if pos == 1 :
                return head.next 

            count = 0 

            curr = head 

            while count < pos - 1:
                count += 1
                curr = curr.next
            curr.next = curr.next.next

            return head  
