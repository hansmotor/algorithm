#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 11:23:16 2017

@author: Cong Liu
"""
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
        point=head
        single_node=head
        ckpoint=ListNode(0)
        ckpoint.next=head
        top=head
        once=True
        
        while point.next!=None:
            if point.val<x:
                if once:
                    top=point
                    once=False
                ckpoint=point
                point=point.next
            else:
                if point.next.val>=x:
                    point=point.next
                else:
                    if once:
                        top=point.next
                        once=False
                    single_node=point.next
                    point.next=single_node.next
                    single_node.next=ckpoint.next
                    ckpoint.next=single_node
                    ckpoint=single_node
        if not once:
            return top
        else:
            return head
    
if __name__ =="__main__":
    
    n1=ListNode(1); n2=ListNode(4); n3=ListNode(3)
    n4=ListNode(2); n5=ListNode(5); n6=ListNode(2)
    
    n1.next=n2; n2.next=n3; n3.next=n4;
    n4.next=n5; n5.next=n6;
    
#==============================================================================
#     node=[]
#     ls=[1,4,3,2,5,2]
#     
#     for i in xrange(len(ls)):
#         node.append(ListNode(ls[i]))
#     
#     for i in xrange(len(node)-1):
#         node[i].next=node[i+1]
#==============================================================================
    
    s=Solution()
    
    t=s.partition(n1, 3)
    
    n=t
    
    while n.next!=None:
        print n.val
        n=n.next
        
    print n.val
                    
                
