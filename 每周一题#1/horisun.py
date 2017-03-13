#!/usr/bin/env python
'''
Author: Horisun (Huang ZhenJie)
'''
def change(amount, coins):
    t = [1] + [0] * amount
    for i in coins:
        for j in xrange(i,amount+1):
            t[j] += t[j-i] 
    return t[amount]       


if __name__ == "__main__":
    assert 1 == change(5000,  [1])   
    assert 1 == change(5000,  [5000]) 
    assert 1 == change(10,  [10]) 
    assert 0 == change(2500,  [5000])
    assert 0 == change(3,  [2])
    assert 2 == change(2,  [1,2]) 
    assert 2 == change(3,  [1,2]) 
    assert 3 == change(4,  [1,2]) 
    assert 4 == change(5,  [1,2,5]) 
    print change(50,  [2,3,4,5,6,7,8,9,10,11]) 
    print change(31,  [7,5,3]) 
    print change(500,  [3,2,1]) 
     
    print change(500,  [3,5,7,8,9,10,11]) 
    print change(1000,  [3,5,7,8,9,10,11]) 
    print change(5000,  [3,5,7,8,9,10,11]) 
    print change(5000,  [1,2,3,4,5,6,7,8,9,10,11]) 
    print change(50000,  [1,2,3,4,5,6,7,8,9,10,11]) 
    print change(500000,  [1,2,3,4,5,6,7,8,9,10,11]) 
    print change(5000,  [i for i in xrange(1,501)]) 
