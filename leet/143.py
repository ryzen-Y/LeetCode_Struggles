# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def count(self, head):
        self.current = head
        count = 0

        while self.current is not None:
            count += 1
            self.current = self.current.next

        return count

    def reorderList(self, head: ListNode | None) -> None:

        if not head or not head.next:
            return
        
        length = self.count(head)
        n = (length + 1 )// 2

        curr1 = head
        node = 0

        while curr1 != None:

            node += 1
            if node == n :
                head2 = curr1.next
                curr1.next = None
                break 
            
            curr1 = curr1.next

        curr2 = head2
        prev = None

        while curr2 != None:
            next_node = curr2.next
            curr2.next = prev

            prev = curr2
            curr2 = next_node
        curr2 = prev
        curr1 = head

        while curr2 is not None:

            temp1 = curr1.next
            temp2 = curr2.next

            curr1.next = curr2
            curr2.next = temp1

            curr1 = temp1
            curr2 = temp2
        
            

            

            
