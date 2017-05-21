import math
class Solution(object):
        def poorPigs(self, buchets,minutesToDie, minutesToTest):
                """
                :type buckets: int 
		:type minutesToDie: int
		:type minutesToTest: int
                :rtype: int 
                """
		return int(math.ceil(math.log(buchets, 1+minutesToTest/minutesToDie))) 

if __name__ == "__main__":
        s = Solution()
        f = lambda x,y,z: s.poorPigs(x,y,z)
   	print f(10,3,8)		
