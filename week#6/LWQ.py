class Solution(object):
        def longestIncreasingPath(self, matrix):
                """
                :type matrix: List[int]
                :rtype: int
                """
		length = len(matrix[0])
                wide = len(matrix)	
		nums = [[1 for i in range(length)] for j in range(wide)]
		output = 1
		new_output = 0
		while(True): 	
			for i in range(length):		
				for j in range(wide):
					if nums[j][i] == output:
						centor = matrix[j][i]
						up_num = 0
						down_num = 0
						left_num = 0
						right_num = 0
						up = 0
						down = 0
						left = 0
						right = 0
						if j == 0:
							up_num = 0
							up = matrix[j][i]
							down = matrix[j+1][i]
							down_num = nums[j+1][i]
						elif j == wide -1:
							up = matrix[j-1][i]
							up_num = nums[j-1][i]
							down_num = 0
							down = matrix[j][i]
						else:
							up = matrix[j-1][i]
							up_num = nums[j-1][i]
							down = matrix[j+1][i]
							down_num = nums[j+1][i]
						if i == 0:
							left = matrix[j][i]
							left_num = 0
							right = matrix[j][i+1]
							right_num = nums[j][i+1]
						elif i == length -1:
							left = matrix[j][i-1]
							left_num = nums[j][i-1]
							right = matrix[j][i]
							right_num = 0
						else:
							left = matrix[j][i-1]
							left_num = nums[j][i-1]
							right = matrix[j][i+1]
							right_num = nums[j][i+1]
						if (left_num >= output and left < centor) or (right_num >= output and right < centor ) or (up_num >= output and up < centor) or (down_num >= output and down < centor) :
							new_output = output + 1
							nums[j][i] = new_output
			if new_output > output:
				output = new_output
			else:
				break
			if output > 5:
				break
		return output	


if __name__ == "__main__":
        s = Solution()
        f = lambda x: s.longestIncreasingPath(x)
	assert 4 == f([[9,9,4],[6,6,8],[2,1,1]])
	assert 4 == f([[3,4,5],[3,2,6],[2,2,1]])
	assert 1 == f([[1,1,1],[1,1,1],[1,1,1]])
	assert 3 == f([[1,1,1],[2,2,2],[3,3,3]])
	assert 4 == f([[1,1,1],[0,0,0],[1,2,3]])
