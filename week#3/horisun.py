class Solution(object):
    def numDecodings(self, s):
        s = map(int, s)
        l = len(s)

        if(l == 0):
            return 0
        if(s[0] == 0):
            return 0
        if(l == 1):
            return 1

        t = [0] * l
        t[0] = 1

        if(s[0] == 0):
            return 0
        else:
            if(s[1] == 0):
                if(s[0]>2):
                    return 0
                else:
                    t[1] = 1
            else:
                if(s[0] == 1):
                    t[1] = 2
                elif(s[0] == 2):
                    if(s[1] > 6):
                        t[1] = 1
                    else:
                        t[1] = 2
                else:
                    t[1] = 1

        i = 2

        while( i<l ):
            #t[i] = t[i-1]
            if(s[i] == 0):
                #print s,i
                if(s[i-1] > 2 or s[i-1] == 0): # ==00 or >=30 , invalid
                    return 0
                else: # 20 or 10
                    #if(i>1):
                    t[i] = t[i-2]
            else: # I'm not 0
                if(s[i-1] == 0): # but the last one is 0
                    t[i] = t[i-1]
                elif(s[i-1]==1): # [10,19]
                        t[i] = t[i-1] + t[i-2]
                elif(s[i-1]==2):  
                    if(s[i] < 7): # [21,26]
                        t[i] = t[i-1] + t[i-2]
                    else: # [27,29] invalid
                        t[i] = t[i-1]
                else:
                    t[i] = t[i-1]
            i += 1

        return t[l-1]



if __name__ == "__main__":
    s = Solution()
    f = lambda x: s.numDecodings(x)
    assert 0 == f("0")
    assert 1 == f("1")
    assert 1 == f("10")
    assert 1 == f("20")
    assert 0 == f("30")
    assert 0 == f("01")
    assert 0 == f("020")
    assert 0 == f("030")
    assert 0 == f("130")
    assert 1 == f("120")
    assert 2 == f("12012")
    assert  96 == f("213201424147191024")
    assert 240 == f("14221422319194918")
    assert 160 == f("169201418147162113")
    assert  64 == f("24191018161781668")
    assert 320 == f("161822127724181318")
    assert   8 == f("6281558142375")
    assert 320 == f("171225515182317246")
    assert  20 == f("12231452028137")
    assert 160 == f("19241123241817964")
    assert  80 == f("316182421239722")
    assert  96 == f("14832151725142320")
    assert 320 == f("18917182421161814")
    assert  64 == f("141410182510913722")
    assert  16 == f("79643158161819")
    assert 384 == f("1522325191923102522")
    assert 200 == f("255122361911161019")
    assert 780 == f("221115141422248225")
    assert  64 == f("104241813141420822")
    assert 120 == f("1821513165412197")
    assert 160 == f("109192519151792122")
