#!/bin/env/python

class method1:
    def f(self,a):
        l = len(a)
        if(l < 2):
            return False
        cut = lambda x: (x%l) if (x>=l) else ((x+l) if (x<0) else (x))
    
        start = True
        k = 0
        j = 0
        i = 0
        dir_ = True
        while(True):
            
            #print k,j,i,dir_,a
            #print "/--"
            while(start): # while loop 2
                #print k,j,i,dir_,a,"start"
                dir_ = a[k]>0
                j = cut(k+a[k])
                if (dir_ != (a[j]>0)):
                    a[k] = 0
                    k = j
                    #print k,j,i,dir_,a
                    continue
                elif (a[j]==0 or (j==k)):
                    a[k] = 0
                    k0 = k
                    while(not a[k]):
                        k = cut(k+1)
                        if(k==k0):
                            return False
                    #print k,j,i,dir_,a
                    continue

                i = cut(j+a[j])
                if(dir_ != (a[i]>0)):
                    a[k] = a[j] = 0
                    k = i
                    #print k,j,i,dir_,a
                    continue
                elif (a[i]==0 or (i==j)):
                    a[j] = 0
                    a[k] = 0
                    k0 = k
                    while(not a[k]):
                        k = cut(k+1)
                        if(k==k0):
                            return False
                    #print k,j,i,dir_,a
                    continue
                elif(i==k):
                    return True
                else:
                    a[k] += a[j]
                    start = False
                    #print k,j,i,dir_,a,"end"
                    #break
            #print "--/"
            #print k,j,i,dir_,a
            # while loop 2
            k = j
            j = i
            i = cut(i+a[i])
            if(i==j):
                a[j] = 0
                a[k] = 0
                i0 = i
                while(not a[i]):
                    i = cut(i+1)
                    if(i==i0):
                        return False
            elif(dir_ != (a[i]>0)):
                a[k] = a[j] = 0
                k = i
                start = True
                continue
            elif(i==k):
                return True
            else:
                a[k] += a[j]
                continue
                



class method2:
    # jump 1 & jump 2 solution
    def f(self,a):
        l = len(a)
        if(l < 2):
            return False
        cut = lambda x: (x%l) if (x>=l) else ((x+l) if (x<0) else (x))


        def ok(i,dir_):
            return (a[i] and((a[i]>0)==dir_))

        def findstart(i):
            j = i
            while(not a[j]):
                j = (j+1)%l
                if(j==i):
                    return -1
            return j
            
        j1 = 0
        j2 = j1
        dir_ = (a[j1]>0)
        while(True):
            # j2 explore first.
            # one step j2, one step j1.
            #
            # if j2 finds the terminal, 
            # it will stop there and every step between
            # j1 and j2 will be set as 0
            # 
            # if j2 meets j1, a loop occurs

            #print "start",
            #old = (j1,j2,a)
            #print j1,j2,a
            j2_ = cut(j2 + a[j2])
            if(j2_ == j2):
                a[j2_] = 0
            if(not ok(j2_,dir_)):
                # j1 to j2 all 0
                while(j1 != j2):
                    j1_ = cut(j1 + a[j1])
                    a[j1] = 0
                    j1 = j1_
                a[j1] = 0
                # findstart(j1)
                j1 = findstart(j1)
                if(j1 < 0):
                    return False
                else:
                    j2 = j1
                    dir_ = (a[j1]>0)
                #print "b j2_",j1,j2,a
                continue

            j2__ = cut(j2_ + a[j2_])
            if(j2__ == j2_):
                a[j2__] = 0
            if(not ok(j2__,dir_)):
                # j1 to j2_ all 0
                while(j1 != j2_):
                    j1_ = cut(j1 + a[j1])
                    a[j1] = 0
                    j1 = j1_
                a[j1] = 0
                # findstart(j1)
                j1 = findstart(j1)
                if(j1 < 0):
                    return False
                else:
                    j2 = j1
                    dir_ = (a[j1]>0)
                #print "bj2__",j1,j2,a
                continue

            j2 = j2__
            j1 = cut(j1 + a[j1])
            #print "ok   ",j1,j2,a,j2==j1,"wtf"

            if(j2 == j1):
                #print "wth"
                return True
        return False

            

def test(G):
    g = G()
    import traceback
    try:
        assert False  == g.f([])
        assert False  == g.f([0])
        assert False  == g.f([1])
        assert False  == g.f([2])
        assert False  == g.f([0,2])
        assert False  == g.f([2,3])
        for k in xrange(2,100):
            assert True  == g.f([1 for i in xrange(k)])

        assert True  == g.f([  2, -1,  1,  2,  2 ])
        assert True  == g.f([  1,  1, -2,  1,  4 ])
        assert True  == g.f([  1,  2,  3,  4,  5 ])
        assert True  == g.f([  2, -1,  2,  2,  3 ])
        assert True  == g.f([  1,  1,  2         ])
        assert True  == g.f([  3,  1,  2         ])
        assert True  == g.f([  2, -2,  2, -2, -1 ])
        assert True  == g.f([  1,  2,  2,  5,  3 ])
        assert False == g.f([  2, -1,  1, -2, -2 ])
        assert False == g.f([ -1,  2             ])
        assert False == g.f([  2, -1             ])
        assert False == g.f([  3,  3, -1, -1     ])
        assert False == g.f([ -1, -2, -3, -4, -5 ])
        print "\033[1m%s \033[32mpassed\033[0m"%G.__name__
    except:
        print "\033[1m%s \033[31mruntime error\033[0m"%G.__name__
        #print traceback.format_exc()
        #traceback.print_exc()
        print '\n'.join(map(lambda x:' '*4+x,traceback.format_exc().split('\n')))

    

if __name__ == "__main__":
    test(method1)
    test(method2)
    #test(Solution3)
