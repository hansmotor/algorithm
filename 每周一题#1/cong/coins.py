#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 17:39:58 2017

@author: Cong Liu
"""
import sys

print "amount:"
amount = input()
print "coins: (please input the values of the coins one by one, and enter 'end' to end)"
coins_ = []
coins_.append(input())
i=1
input_type=coins_[0]

while isinstance(input_type, int):
    coins_.append(input())
    input_type=coins_[i]
    i+=1
    
coins=[0]*(i-1)

for j in range(0, i-1):
    coins[j] = coins_[j]

coins=list(set(coins))
coins=sorted(coins) 

print('amount:'); print(amount)
print('coins:'); print(coins)

matrix=[]

temp=[0 for j in range (i-1)]



def recursion(ser,ser_ser, temp_amount):
    
    temp[ser]=ser_ser
    temp_amount=temp_amount-ser_ser*coins[ser]
    b=temp_amount
    c=ser
    
    total_num=0
    
    for j in range (0, i-1):
        total_num+=temp[j]
    
    # print('ser:', c, 'ser_ser:', temp[ser], 'temp_amount:', b)
    
    if(temp_amount==0 and total_num<500):
        string=str(amount)
        string+='='
        for j in range (0, i-1):
            if(temp[j]!=0):
                string+=str(temp[j])
                string+='*'
                string+=str(coins[j])
                string+='+'
        string=string.rstrip('+')
        matrix.append(string)
            
    
    if(c<(len(coins)-1) and b!=0 and total_num<500):
        a=temp_amount//coins[c+1]
        for j in range(0, a+1):
            recursion(c+1, j, b)
    
        


if __name__ == '__main__':
    
    if(amount>5000):
        print "amount is too big"
        sys.exit(0)
    
    if(max(coins)>5000):
        print "there is a coin that is too big"
        sys.exit(0)
    
    big_ser=amount//coins[0]
    
    for j in range(0, big_ser+1):
        recursion(0, j, amount)
    
    ch=str(len(matrix))
    st='there are '
    st+=ch
    st+=' methods:'
    
    if(len(matrix)>0):
        print(st)
    
    for j in range(0, len(matrix)):
        print(matrix[j])
   
    st=st.rstrip(':')
    st+=', assuming that the number of the coins is less than 500'
    print(st)    