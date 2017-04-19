# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        odd = head
        even = head.next
        while even != None and odd != None:
            c = odd.val
            odd.val = even.val
            even.val = c
            odd = even.next
            if odd != None:
                even = odd.next
        return head