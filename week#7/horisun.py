# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if(not head):
            return head
        p = head
        a = ListNode(None)
        b = ListNode(None)
        a_ = a
        b_ = b
        t = None
        while(p):
            if(p.val<x):
                a.next = p
                a = p
                t = p.next
                p.next = None
                p = t
            else:
                b.next = p
                b = p
                t = p.next
                p.next = None
                p = t

        a.next = b_.next
        return a_.next
