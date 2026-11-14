# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def size(self, head):
        curr = head
        count =  0
        while curr != None:
            count += 1
            curr = curr.next
        return count 

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = self.size(head)
        pos = (length + 1) - n 
        if pos == 1 :
            return head.next

        curr =  head 
        count =  1 

        while count < pos - 1 :
            
            curr = curr.next
            count += 1
            
            
            
        curr.next = curr.next.next

        return head 

        

        