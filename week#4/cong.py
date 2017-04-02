#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 18:54:05 2017

@author: Cong Liu
"""

import sys

print "array: (for example [4,3,2,7,8,2,3,1])"

array=input()

if(max(array)>len(array)):
    print 'there is a number that is bigger than n'
    sys.exit(0)
if(min(array)<1):
    print 'there is a number that is less than 1'
    sys.exit(0)

class Solution(object):
    def findDisappearedNumbers(self, nums):
        for i in range(len(nums)):
            
            nums[(nums[i]%len(nums))-1]-=len(nums)
            
#==============================================================================
#             if(nums[i]>0):
#                 nums[nums[i]-1]-=len(nums)
#             else:
#                 nums[nums[i]+len(nums)-1]-=len(nums)
#==============================================================================

#==============================================================================
#             a=nums[i]
#             while(a<=0):
#                 a+=len(nums)
# 
#             nums[a-1]-=len(nums)
#==============================================================================
                        
        back=[]
        
        for i in range(len(nums)):
            if(nums[i]>0):
                back.append(i+1)
                
        return back
    
    
if __name__ == '__main__':
    
    solu=Solution()
    
    assert [5,6]==solu.findDisappearedNumbers([4,3,2,7,8,2,3,1])
    assert [1]==solu.findDisappearedNumbers([3,3,2,4,5,6])
    assert [4]==solu.findDisappearedNumbers([3,1,6,5,3,2])
    assert [3,6]==solu.findDisappearedNumbers([4,4,2,1,5,5])
    assert [6,9]==solu.findDisappearedNumbers([1,4,2,3,2,3,5,8,7])
    assert [2,5,7]==solu.findDisappearedNumbers([10,8,6,10,3,4,6,1,9,4])
    assert [6,7,8]==solu.findDisappearedNumbers([9,4,2,5,3,5,1,1,3])
    assert [2,7]==solu.findDisappearedNumbers([3,5,3,1,6,1,4])
    assert [1,5]==solu.findDisappearedNumbers([4,2,6,9,6,3,8,9,7])
    assert [9]==solu.findDisappearedNumbers([3,2,3,5,7,6,4,8,1])
    assert [4,6,9]==solu.findDisappearedNumbers([10,10,5,7,3,5,2,7,1,8])
    assert [1,3]==solu.findDisappearedNumbers([4,6,2,8,6,7,7,5])
    assert [4,6,10]==solu.findDisappearedNumbers([11,5,2,3,7,8,8,9,1,5,3])
    assert [2,5,7]==solu.findDisappearedNumbers([9,8,9,8,6,1,3,4,6])
    
    answer=solu.findDisappearedNumbers(array)
    print 'answer:', answer