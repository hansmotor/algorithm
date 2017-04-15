#!/usr/bin/env

class Solution(object):

    dir_ = (( 0,-1),
            ( 0, 1),
            (-1, 0),
            ( 1, 0))
        

    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        self.m = m = matrix
        if(not m):
            return 0
        self.row = row = len(m)
        if(not row):
            return 0
        self.col = col = len(m[0])
        if(not col):
            return 0

        self.mm = mm =[[0]*col for i in xrange(row)]

        for r in xrange(row):
            for c in xrange(col):
                if(mm[r][c]):
                    continue
                else:
                    self.proc(r,c)

        res = max(map(max,mm))
        #print mm
        return res

    def proc(self,r,c):
        m = self.m
        mm = self.mm

        if(mm[r][c]<0):
            return 1
        if(mm[r][c]>0):
            return mm[r][c]

        
        row = self.row
        col = self.col

        dir_ = self.dir_

        p = []
        for ri,ci in dir_:
            rn = r+ri
            if(rn<0 or rn>=row):
                continue
            cn = c+ci
            if(cn<0 or cn>=col):
                continue

            if(m[rn][cn] <= m[r][c]):
                continue
            else:
                p.append(self.proc(rn,cn))
        if(p):
            res = max(p)+1
            #print p
        else:
            res = 1
            #print p

        mm[r][c] = res
        return res

                        
                        
                    
                    
if __name__ == "__main__":
    s = Solution()
    l = s.longestIncreasingPath
    assert 4 == l([[9,9,4],
                   [6,6,8],
                   [2,1,1]])
    assert 4 == l([[3,4,5],
                   [3,2,6],
                   [2,2,1]])
    assert 3 == l([[0],
                   [1],
                   [5],
                   [5]])
    assert 1 == l([[1]])
