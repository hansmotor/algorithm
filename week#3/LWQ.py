class Solution(object):
	def numDecodings(self,s):
		"""
		:type s: str
		:rtype: int
		"""
        	temp = list(s)
		msg = [int(i) for i in temp]
		num = [0] * (len(msg)+1)
        	num[0] = 1
		if (msg[0] == 0):
			return 0
	        for i in range (1,len(msg)+1):
        		if (msg[i-1] !=0):
				num[i] += num[i-1]
			if (i>=2 and msg[i-2] * 10 + msg[i-1] >=10 and msg[i-2] * 10 + msg[i-1] <= 26):
				num[i] += num[i-2]
			if (num[i] == 0):
				return 0
		return num[len(msg)]
			

if __name__ == "__main__":
        s = Solution()
	f = lambda x: s.numDecodings(x)
	assert 3 == f("111")
	assert 0 == f("1001")
  	assert 0 == f("0")
    	assert 1 == f("1")
    	assert 1 == f("10")
    	assert 200 == f("255122361911161019")
    	assert 780 == f("221115141422248225")
    	assert  64 == f("104241813141420822")
    	assert 120 == f("1821513165412197")
    	assert 160 == f("109192519151792122")
	assert 2 == f("12")
