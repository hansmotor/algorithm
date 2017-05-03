# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


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



def array2list(a):
    if(not a):
        return None
    elif(len(a)==1):
        return ListNode(a[0])
    else:
        p = ListNode(a[0])
        b = p
        for i in a[1:]:
            p.next = ListNode(i)
            p = p.next
        return b

def list2array(a):
    r = []
    while(a):
        r.append(a.val)
        a = a.next
    return r

def test(l,a,b,c):
    assert list2array(l(array2list(b),a)) == c

if __name__ == "__main__":
    s = Solution()
    l = s.partition
    test(l,0,[1,4,3,2,5,2],[1,4,3,2,5,2])
    test(l,1,[1,4,3,2,5,2],[1,4,3,2,5,2])
    test(l,2,[1,4,3,2,5,2],[1,4,3,2,5,2])
    test(l,3,[1,4,3,2,5,2],[1,2,2,4,3,5])
    test(l,4,[1,4,3,2,5,2],[1,3,2,2,4,5])
    test(l,5,[1,4,3,2,5,2],[1,4,3,2,2,5])
    test(l,6,[1,4,3,2,5,2],[1,4,3,2,5,2])
    test(l,6,[],[])
    test(l,6,[0],[0])
    test(l,6,[6],[6])
    test(l,6,[7],[7])
    test(l,0,[1,-1],[-1,1])
