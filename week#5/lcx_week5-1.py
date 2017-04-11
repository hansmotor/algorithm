#!/usr/bin/env python

class Solution(object):
	
	def threeSum(self,nums):
		nums.sort()
		N_list=[]
		P_list=[]
		triplets=[]
		test_list=[]
		for i in xrange(len(nums)-1):
			if nums[i]==0:
				zero_site=i
				N_list=nums[:i]			
				P_list=nums[i+1:]
				for i in xrange(len(N_list)):
					if abs(N_list[i]) in P_list:
						triplets.append([N_list[i],0,-N_list[i]])
			if (nums[i]<0) and (nums[i+1]>0):
					N_list=nums[:i+1]
					P_list=nums[i+1:]	
		for i in xrange(len(N_list)):
			for j in xrange(len(P_list)):
				add_two=N_list[i]+P_list[j]
				if add_two<0:
					test=P_list[j]
					P_list[j]=0
					if(abs(add_two) in P_list):
						triplets.append([N_list[i],P_list[j],abs(add_two)])
					P_list[j]=test
				elif add_two > 0:
					test=N_list[i]
					N_list[i]=0
					if (-add_two) in N_list:
						triplets.append([N_list[i],P_list[j],-add_two])
					N_list[i]=test
		print triplets	
		for i in triplets:
			if not i in test_list:
				test_list.append(i)

		print test_list

if __name__=="__main__":
	S=[-1,0,1,2,-1,-4]
	test=Solution()
	test.threeSum(S)
			
	
