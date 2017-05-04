# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False
        one = head
        two = head
        while two != None:
            one = one.next
            if two.next != None:
                two = two.next.next
            else:
                return False
            if one == two:
                return True
        return False