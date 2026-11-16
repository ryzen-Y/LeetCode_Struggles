# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        
        dummy = ListNode()
        dummy.next = head 
        before = dummy
        count = 1
        curr = head 

        while count < left :

            before = curr
            count += 1
            curr = curr.next
        
        
        prev = None 
        first = curr
        while left <= right:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            left += 1

        before.next = prev
        first.next = curr

        return dummy.next

           

            



        