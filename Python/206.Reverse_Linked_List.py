# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return []
        c = head
        arr = []
        while c != None:
            arr.append(c.val)
            c = c.next
        c = head
        while c != None:
            c.val = arr.pop()
            c = c.next
        return head