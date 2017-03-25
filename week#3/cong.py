#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 17:25:02 2017

@author: Cong Liu
"""

print "array: (please input the values one by one, and enter 'end' to end)"
code = []
code.append(input())
i=1
input_type=code[0]

while isinstance(input_type, int):
    code.append(input())
    input_type=code[i]
    i+=1
    
codes=[0]*(i-1)

for j in range(0, i-1):
    codes[j] = code[j]

print('codes:'); print(codes)

def condition(a):
    if(a[0]*10+a[1]<27):
        return True
    else:
        return False

def recursion(array):
    
    if(len(array)>1):
        if(array[0]<1 or array[1]<0):
            return 0
    elif(array[0]<1):
        return 0
    
    if(len(array)==1):
        return 1
    if(len(array)==2):
        if(array[1]>0):
            if(condition(array)):
                return 2
            else:
                return 1
        else:
            if(condition(array)):
                return 1
            else:
                return 0
    
    
    arr=list(array)
    
    if(condition(array)):
        del arr[0]
        x=recursion(arr)
        del arr[0]
        x=x+recursion(arr)
        return x
    else:
        del arr[0]
        return recursion(arr)
        


if __name__ == '__main__':
    
    codes0=[1,2,1,2,0]
    codes1=[0,1,2,1,2]
    codes2=[1,2,3,0,1,2]
    codes3=[1,2,5,-1,3,1]
    codes4=[1,2,2,2,3,0]
    
    codes5=[1]
    codes6=[1,1]
    codes7=[1,1,1]
    codes8=[1,1,1,1]
    codes9=[1,1,1,1,1]
    codes10=[1,1,1,1,1,1]
    
    assert 3==recursion(codes0)
    assert 0==recursion(codes1)
    assert 0==recursion(codes2)
    assert 0==recursion(codes3)
    assert 0==recursion(codes4)
    
    assert 1==recursion(codes5)
    assert 2==recursion(codes6)
    assert 3==recursion(codes7)
    assert 5==recursion(codes8)
    assert 8==recursion(codes9)
    assert 13==recursion(codes10)
    
    
    amount=recursion(codes)
    print 'number of ways to decode it:', amount