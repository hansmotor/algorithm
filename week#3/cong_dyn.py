#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 15:40:40 2017

@author: Cong Liu
"""
print "array:"

codes=input()

def dynam(array):
    
    array=map(int, array)
    
    if(len(array)<1):
        return 0
    if(array[0]<1):
        return 0

    ls=[1]+[0]*len(array)
        
    for i in range(len(array)):
        
        ser=-1*i-1
        
        if(array[ser]<0):
            return 0
        
        if(i==0):
            if(array[-1]>0):
                ls[i+1]=1
            else:
                ls[i+1]=0
        else:
            if(array[ser]<1):
                ls[i+1]=0
            elif(array[ser]*10+array[ser+1]<27):
                ls[i+1]=ls[i]+ls[i-1]
            else:
                ls[i+1]=ls[i]

    return ls[-1]



if __name__ == '__main__':
    
    assert 0 == dynam("0")
    assert 1 == dynam("1")
    assert 1 == dynam("10")
    assert 1 == dynam("20")
    assert 0 == dynam("30")
    assert 0 == dynam("01")
    assert 0 == dynam("020")
    assert 0 == dynam("030")
    assert 0 == dynam("130")
    assert 1 == dynam("120")
    assert 2 == dynam("12012")
    assert  96 == dynam("213201424147191024")
    assert 240 == dynam("14221422319194918")
    assert 160 == dynam("169201418147162113")
    assert  64 == dynam("24191018161781668")
    assert 320 == dynam("161822127724181318")
    assert   8 == dynam("6281558142375")
    assert 320 == dynam("171225515182317246")
    assert  20 == dynam("12231452028137")
    assert 160 == dynam("19241123241817964")
    assert  80 == dynam("316182421239722")
    assert  96 == dynam("14832151725142320")
    assert 320 == dynam("18917182421161814")
    assert  64 == dynam("141410182510913722")
    assert  16 == dynam("79643158161819")
    assert 384 == dynam("1522325191923102522")
    assert 200 == dynam("255122361911161019")
    assert 780 == dynam("221115141422248225")
    assert  64 == dynam("104241813141420822")
    assert 120 == dynam("1821513165412197")
    assert 160 == dynam("109192519151792122")
    
    assert 3==dynam('12120')
    assert 0==dynam('01212')
    assert 0==dynam('123012')
    assert 0==dynam('122230')
    
    assert 1==dynam('1')
    assert 2==dynam('11')
    assert 3==dynam('111')
    assert 5==dynam('1111')
    assert 8==dynam('11111')
    assert 13==dynam('111111')
    
    amount=dynam(codes)
    print 'amount:', amount
