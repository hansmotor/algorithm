#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 11:35:38 2017

@author: Cong Liu
"""

class Solution(object):
    def longestIncreasingPath(self, matrix, tp):
        m=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                location=i*len(matrix[i])+j
                length=len(matrix[i])
                if(j-1>=0 and matrix[i][j]<matrix[i][j-1]): #left
                    m.append([location, location-1])
                if(i-1>=0 and matrix[i][j]<matrix[i-1][j]): #up
                    m.append([location, location-length])
                if(j+1<length and matrix[i][j]<matrix[i][j+1]): #right
                    m.append([location, location+1])
                if(i+1<len(matrix) and matrix[i][j]<matrix[i+1][j]): #down
                    m.append([location, location+length])

        b=[]
        c=list(m)
        
        i=0
        while i<len(c):
            for j in range(len(m)):
                if(c[i][0]==m[j][1]):
                    del c[i]
                    i-=1
            i+=1
        
        while len(c)>0:
            b=list(c)
            c=[]
            for i in range(len(b)):
                for j in range(len(m)):
                    if(b[i][-1]==m[j][0]):
                        temp=list(b[i])
                        temp.append(m[j][1])
                        c.append(temp)
                        
        back=[]
        for i in range(len(b)):
            back.append([])
            for j in range(len(b[i])):
                temp_ans=matrix[b[i][j]//length][b[i][j]%length]
                back[i].append(temp_ans)
                
        if tp=='a':
            return back
        if tp=='b':
            return b
        if tp=='c' and len(b)>0:
            return len(b[0])
        
        return 1
        
                
if __name__ == '__main__':
    s=Solution()
    answer1=s.longestIncreasingPath([[9,9,4],
                                     [6,6,8],
                                     [2,1,1]], 'c')
    
    answer2=s.longestIncreasingPath([[3,4,5],
                                     [3,2,6],
                                     [2,2,1]], 'c')
    
    answer3=s.longestIncreasingPath([[9,9,9],
                                     [1,1,1]], 'c')
    
    answer4=s.longestIncreasingPath([[9,9,9],
                                     [9,9,9]], 'c')
    
    answer5=s.longestIncreasingPath([[9,8,7],
                                     [4,5,6]], 'c')
    
    answer6=s.longestIncreasingPath([[2,4,3,1],
                                     [3,5,2,1],
                                     [7,6,8,1],
                                     [8,3,4,5]], 'c')
    
    answer7=s.longestIncreasingPath([[2,4,3,1],
                                     [3,5,2,1],
                                     [7,6,8,1],
                                     [8,3,4,5]], 'a')
    
    assert 4==answer1; assert 4==answer2; assert 2==answer3;
    assert 1==answer4; assert 6==answer5; assert 8==answer6;
    assert [[1,2,3,4,5,6,7,8]]==answer7