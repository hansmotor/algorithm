#!/usr/bin/env python

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #print "-------"

        n = nums
        n.sort()
        l = len(n)
        res = []
        last = None

        #print n

        for i in xrange(l):
            if(i):
                if(n[i] == last):
                    continue
            c = -n[i]
            j = i+1
            k = l-1
            while(j<k):

                while(n[j]+n[k]<c and j<k):
                    j+=1
                while(n[j]+n[k]>c and k>j):
                    k-=1

                if(k<=j):   
                    break

                if(n[j]+n[k]==c):
                    res.append([n[i],n[j],n[k]])
                    while(j+1<k and n[j+1]==n[j]):
                        j+=1
                    while(k-1>j and n[k-1]==n[k]):
                        k-=1

                    j+=1
                    k-=1

            last = n[i]

        #print "======"
        return res


if __name__ == "__main__":
    s = Solution()
    t = s.threeSum
    print t([-1,0,1,-1,2,4])
    print t([-1,0,1,2,-1,-4])     
    print t([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0])            
