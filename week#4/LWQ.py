class Solution(object):
	def findDisappearedNumbers(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		output = []
		i = 0
		while i < len(nums):	
			if (nums[i] > 0):
				index = nums[i] - 1
				if (nums[index]>0):
					nums[i] = nums[index]
					nums[index] = -1
				else:
					nums[i] = 0
					nums[index] -= 1
					i += 1
			else:
				i +=1	
		for j in range(len(nums)):
			if (nums[j] == 0):
				output.append(j +1) 
		return output		

if __name__ == "__main__":
        s = Solution()
	f = lambda x: s.findDisappearedNumbers(x)
	assert [4] == f([1,2,3,3])
	assert [5,6] == f([4,3,2,7,8,2,3,1])
  	assert [1,3,7,9] == f([5,6,5,2,2,8,4,8,5])
    	assert [10,11,12] == f([3,2,1,5,5,9,7,1,3,4,8,6])
    	assert [] == f([5,3,2,4,1,6])
    	assert [1,2,3] == f([4,4,5,5,6,6])
