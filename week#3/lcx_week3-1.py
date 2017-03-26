#!/usr/bin/env python
import string

class Solution(object):
	def numDecodings(self,s):
		s_list=map(string.atoi,list(s))
		num=[1]+[0]*(len(s)-1)
		if s_list[1]==0:
			num[1]=1
		elif s_list[0]*10+s_list[1]<27:
			num[1]=2
		else:
			num[1]=1
		for i in xrange(2,len(s)):
			if s_list[i]!=0:
				num[i]+=num[i-1]
			if i>=2 and s_list[i-1]*10+s_list[i]>9 and s_list[i-1]*10+s_list[i]<27:
				num[i]+=num[i-2]	
		print 'num',num
		return num[-1]


if __name__=="__main__":
	result=Solution()
	print "hehe_result",result.numDecodings('2551223619111610019')
	f=lambda x:result.numDecodings(x)
	assert 3==f('111')
	assert 0==f('1001')
	assert 1==f('10')
	assert 200==f('255122361911161019')
	assert 780==f('221115141422248225')
