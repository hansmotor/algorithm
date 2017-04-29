class ListNode(object):
	def __init__(self,data):
		self.data = data
		self.next = None

class Solution(object):
        def partition(self, head, x):
                """
                :type head: ListNode
		:type x: int
                :rtype: ListNode
                """
		if head == None: return None
		flag1,flag2 = False,False
		p1 = p2 = ListNode(None)
		while(head):
			curr,head = head,head.next
			if curr.data < x:
				if flag1:
					p1.next = curr
					p1 = p1.next
					p1.next = None
				else:
					p1 = headp1 = curr
					p1.next = None
					flag1 = True
			else:
                                if flag2:
					p2.next = curr
					p2 = p2.next
					p2.next = None
                                else:
					p2 = headp2 = curr
					p2.next = None
                                        flag2 = True
		p1.next = headp2
		return headp1	

if __name__ == "__main__":
        s = Solution()
        f = lambda head,x: s.partition(head,x)
	head1 = ListNode(1)
	head2 = head1
	head1.next = ListNode(4)
	head1 = head1.next
	head1.next = ListNode(3)	
	head1 = head1.next
	head1.next = ListNode(2)	
	head1 = head1.next
	head1.next = ListNode(5)	
	head1 = head1.next
	head1.next = ListNode(2)	
	head1 = head1.next
	head1.next = None
	head3 = f(head2,3)
	while head3:
		print head3.data
		head3 = head3.next
		
