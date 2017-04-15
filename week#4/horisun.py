class Solution(object):
    def findDisappearedNumbers(self, a):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(a)
        i = 0
        c = 0
        r = []
        #print a
        while(i<l):# and c<10):
            c += 1
            if(a[i]==i+1 or a[i]==0):
                i += 1
            else:
                j = a[i]-1
                #print j,i
                if(a[j]!=a[i]):
                    a[j],a[i] = a[i],a[j]
                else:
                    a[i] = 0
                    i += 1
            #print a,i

        for i in xrange(l):
            if(a[i]==0):
                r.append(i+1)

        #print r
        return r
