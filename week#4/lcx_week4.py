#!/usr/bin/env python

class Solution(object):
	
	def findDisappearedNumbers(self,nums):
		nums.sort()
		re_list=[]
		for i in xrange(len(nums)-1):
			diff=nums[i+1]-nums[i]
			if diff>1:
				hehe=nums[i]
				for i in xrange(1,diff):
					re_list.append(hehe+i)
		print re_list

if __name__=="__main__":
	list1=[4,3,2,7,8,2,3,1]
	test=Solution()
	test.findDisappearedNumbers(list1)
				
				
