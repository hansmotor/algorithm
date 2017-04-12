#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 17:22:09 2017

@author: Cong Liu
"""

print "array: (for example [-1, 0, 1, 2, -1, -4])"

array=input()


class Solution(object):
    
                       
    def threeSum(self, nums):
        neg=[]
        pos=[]
        zero=[]
        
        back=[]
        back_zero=[] 
        
        for i in range(len(nums)):
            if(nums[i]>0):
                pos.append(nums[i])
            elif(nums[i]<0):
                neg.append(nums[i])
            else:
                zero.append(nums[i])
                
        if(len(zero)>2):
            back.append([0,0,0])
        
        if(len(pos)<1 or len(neg)<1):
            return back
        
        length=max(-1*min(neg)+1,max(pos)+1)
        array_neg=[0 for i in range(length)]
        array_pos=[0 for i in range(length)]
        
        for i in range(len(neg)):
            array_neg[-1*neg[i]]+=1
        for i in range(len(pos)):
            array_pos[pos[i]]+=1
                     
        
        
        neg_temp=list(set(neg))
        
        for i in range(len(neg_temp)):
            temp_pos=list(array_pos)
            if(temp_pos[-1*neg_temp[i]]>0):
                back_zero.append([neg_temp[i], 0, -1*neg_temp[i]])
            for j in range(1, -1*neg_temp[i]+1):
                if(temp_pos[j]>0 and temp_pos[-1*neg_temp[i]-j]>0):
                    if(j!=-1*neg_temp[i]-j):
                        back.append([neg_temp[i], j, -1*neg_temp[i]-j])
                        temp_pos[j]=0
                        temp_pos[-1*neg_temp[i]-j]=0
                    elif(temp_pos[j]>1):
                        back.append([neg_temp[i], j, j])
                        temp_pos[j]=0
                                
        pos_temp=list(set(pos))
                                
        for i in range(len(pos_temp)):
            temp_neg=list(array_neg)
            for j in range(1, pos_temp[i]+1):
                if(temp_neg[j]>0 and temp_neg[pos_temp[i]-j]>0):
                    if(j!=pos_temp[i]-j):
                        back.append([pos_temp[i], -1*j, j-pos_temp[i]])
                        temp_neg[j]=0
                        temp_neg[pos_temp[i]-j]=0
                    elif(temp_neg[j]>1):
                        back.append([pos_temp[i],-1*j, -1*j])
                        temp_neg[j]=0
        
        if(len(zero)>0):
            back=back+back_zero
        
        return back
    
    
    
if __name__ == '__main__':
    
    s=Solution()
    f=lambda x: s.threeSum(x)
#    array=[-1, 0, 1, 2, -1, -4]
    in1=[4,6,-5,3,7,-4,-2,-3,0,0,0]
    in2=[-1, 0, 1, 2, -1, -4]
    in3=[3, 5, 2, 6, 8, 9]
    in4=[3, 5, 4, 0, 0, 0]
    in5=[0,0,0,0,0]
    in6=[5,-4,1,-2,4,-3,6,-3,0]
    in7=[1,-2,3,-4,-1,2,0,0,0,0]
    in8=[-1,-1,-1,-1,1,1,1,1,5,2,5,3,-2,-3,-2,0]
    
    out1=[[0, 0, 0], [6, -2, -4], [7, -2, -5], [7, -3, -4], [-4, 0, 4], [-3, 0, 3]]
    out2=[[2, -1, -1], [-1, 0, 1]]
    out3=[]
    out4=[[0, 0, 0]]
    out5=out4
    out6=[[5, -2, -3], [6, -2, -4], [6, -3, -3], [-4, 0, 4]]
    out7=[[0, 0, 0], [-4, 1, 3], [3, -1, -2], [-1, 0, 1], [-2, 0, 2]]
    out8=[[-2, 1, 1], [-3, 1, 2], [2, -1, -1], [3, -1, -2],\
          [5, -2, -3], [-2, 0, 2], [-1, 0, 1], [-3, 0, 3]]
    
    assert out1==f(in1)
    assert out2==f(in2)
    assert out3==f(in3)
    assert out4==f(in4)
    assert out5==f(in5)
    assert out6==f(in6)
    assert out7==f(in7)
    assert out8==f(in8)

    answer=f(array)
    print 'answer:', answer

