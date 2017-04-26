# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == headB:
            return headA
        if headA and headB:
            a = aa = headA
            b = bb = headB
            counta = 0 
            countb = 0 
            while a.next:
                a = a.next
                counta += 1
            while b.next:
                b = b.next
                countb += 1
            if a == b:
                while counta > countb:
                    aa = aa.next
                    counta -= 1
                while countb > counta:
                    bb = bb.next
                    countb -= 1
                while aa != bb:
                    aa = aa.next
                    bb = bb.next
                return aa
            else:
                return None
        return None