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

matrix=[]

array=[]
aside=[-1]*length
for i in range(length):
    array+=[random.randrange(-1, 2, 2)*random.randint(1, 10)]
   
print('array:')
print(array)

array_abs=[0]*length
for i in range(length):
    array_abs[i]=(i+array[i])%(length)
    if(array_abs[i]==i):
        aside[i]=i

the_array=[0]*length

for i in range(length):
    the_array[i]=i

print("array_abs:")
print(array_abs)
print("aside:")
print(aside)

for j in range(length):
    B=False
    for i in range(length):
        if(i!=aside[i]):
            the_array[i]=array_abs[the_array[i]]
            if(the_array[i]==i):
                sym=array[i]//abs(array[i])
                sym_right=True
                y=array_abs[i]
                for l in range(j):
                    if(sym!=array[y]//abs(array[y])):
                        sym_right=False
                        break
                    y=array_abs[y]
                    
                if(sym_right):
                    print("yes")
                    print(i)
                    print(array_abs[i])
                    x=array_abs[i]
                    for k in range(j):
                        print(array_abs[x])
                        x=array_abs[x]
                    B=True
                    break

    if(B):
        break
    elif(j==length-1):
        print("no")
