class Solution(object):
        def threeSum(self, nums):
                """
                :type nums: List[int]
                :rtype: List[List[int]]
                """
		nums.sort()
		num = nums[0] -1		
		output = []
		if len(nums) < 3:
			return output
		for i in range (len(nums)-2):
			if nums[i] > 0 :
				break
			if (nums[i] + nums[len(nums)-1] + nums[len(nums)-2]) < 0:
				continue
			if nums[i] == num :
				continue

			sum_two = 0 - nums[i]
			num = nums[i]	
			
			num_two  =  nums[i+1] - 1;
			for j in range (i+1,len(nums)-1):
				if nums[j] > sum_two:
					break
				if (nums[j] + nums [len(nums)-1]) < sum_two:
					continue
				if nums[j] == num_two:
					continue
				num_two = nums[j]	
				sum_one = sum_two - nums[j]
				for k in range (j+1, len(nums)):
					if nums[k] == sum_one:
			 			output.append([nums[i],nums[j],nums[k]])
						break
		return output	


if __name__ == "__main__":
        s = Solution()
        f = lambda x: s.threeSum(x)
	print f([4,4,4,-1,1,2,-1,-4,5,7,2,2])
	print f([4,4,4,-1,0,1,2,-1,-4])
	print f([-1,0,1,2,-1,-4])
	print f([0,0,0])
	print f([0,0])
	print f([0,0,1])
