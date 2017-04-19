# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return None
        one = two = head
        while two != None and two.next != None:
            one = one.next
            two = two.next.next
            if one == two:
                break
        else:
            return None
        while head != one:
            one = one.next
            head = head.next
        return head