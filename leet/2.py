class Solution:
    def addTwoNumbers(self, l1, l2):
        curr1 = l1
        curr2 = l2

        dummy = ListNode()
        tail = dummy

        carry = 0

        while curr1 or curr2 or carry:

            if curr1:
                val1 = curr1.val
            else:
                val1 = 0

            if curr2:
                val2 = curr2.val
            else:
                val2 = 0

            total = val1 + val2 + carry

            if total > 9:
                carry = 1
                digit = total - 10
            else:
                carry = 0
                digit = total

            tail.next = ListNode(digit)
            tail = tail.next

            if curr1:
                curr1 = curr1.next

            if curr2:
                curr2 = curr2.next

        return dummy.next