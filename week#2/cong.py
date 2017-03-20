#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 18:15:39 2017

@author: Cong Liu
"""


import sys
import random

print ("please input the length of the array:")

length=input()

if(not isinstance(length, int)):
    print("the length is not an integer")
    sys.exit(0)
    
elif(length<=0):
    print("the length is not positive")
    sys.exit(0)

array=[]
for i in range(length):
    array+=[random.randrange(-1, 2, 2)*random.randint(1, 10)]

print 'array:', array

for i in range(length):
    symbol=array[i]//abs(array[i])
    array[i]=(abs(array[i])%length)*symbol
    

#print 'array:', array

def cal(ser, sym):

    x=array[ser]
    array[ser]=0
    y=ser+x
    y=y%length
    lo=0
    while(array[y]*sym>0 and lo<length):
        x=x+array[y]
        z=array[y]
        y=y+z
        y=y%length
        #if(ser==2):
            #print x, z, y
        if(x%length==0):
            print 'loop from', y
            return True
        lo+=1
        #print(lo)

    return False
        
if __name__ == '__main__':
    
    loop_exist=False
    
    for i in range(length):
        if(array[i]>0):
            loop_exist=cal(i,1)
            if(loop_exist):
                break
        if(array[i]<0):
            loop_exist=cal(i,-1)
            if(loop_exist):
                break
            
    if(loop_exist):
        print('yes')
    else:
        print('no')
    #print 'array:', array
    
