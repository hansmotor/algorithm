class SolutionHoriSun(object):
    def numDecodings(self, s):
        #print "Decoding",s
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
        #print t
        while( i<l ):
            #print i,s[i],t
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
        #print l-1,s[l-1],t
        return t[l-1]


class Solution2(object):
    def numDecodings(self, s):
        l = len(s)
        if(l==0 or s[0]=='0'):
            return 0

        s = map(int,s)
        
        f0 = 1
        f1 = 1
        f2 = 0
        for i in xrange(2,l):
            pass














class SolutionCong(object): 
    def condition(self,a):
        if(a[0]*10+a[1]<27):
            return True
        else:
            return False

    def numDecodings(self, array):
        if(type(array) == str):
            array = map(int, array)
        if(len(array)==0):
            return 0

        if(len(array)>1):
            if(array[0]<1 or array[1]<0):
                return 0
        elif(array[0]<1):
            return 0
        
        if(len(array)==1):
            return 1
        if(len(array)==2):
            if(array[1]>0):
                if(self.condition(array)):
                    return 2
                else:
                    return 1
            else:
                if(self.condition(array)):
                    return 1
                else:
                    return 0
        
        
        arr=list(array)
        
        if(self.condition(array)):
            del arr[0]
            x=self.numDecodings(arr)
            del arr[0]
            x=x+self.numDecodings(arr)
            return x
        else:
            del arr[0]
            return self.numDecodings(arr)
            


class SolutionCong2(object):
    def numDecodings(self, array):
        
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




class SolutionXLZ(object):
	def numDecodings(self,s):
		if(len(s)==0): return 0
        	temp = list(s)
		msg = [int(i) for i in temp]
		num = [0] * (len(msg)+1)
        	num[0] = 1
		if (msg[0] == 0):
			return 0
	        for i in range (1,len(msg)+1):
        		if (msg[i-1] !=0):
				num[i] += num[i-1]
			if (i>=2 and msg[i-2] * 10 + msg[i-1] >=10 and msg[i-2] * 10 + msg[i-1] <= 26):
				num[i] += num[i-2]
			if (num[i] == 0):
				return 0
		return num[len(msg)]





def gen_test(f):
    import random
    for j in xrange(1):
        a = "".join(["%d"%int(random.random()*25+1) for i in xrange(500)])
        s0 = 'assert %3d == f("%s")'%(f(a),a)
        print s0
        t = int(random.random()*(len(a)-1))
        a = a[:t] + '0' + a[t:]
        s1 = 'assert %3d == f("%s")'%(f(a),a)
        print s1
        f = open("wtf","w")
        f.write(s0)
        f.write("\n")
        f.write(s1)
        f.write("\n")
        f.close()


def bundle(f):
    test_examples = (
        ( 0, "" ),
        ( 0, "0" ),
        ( 1, "1" ),
        ( 1, "10" ),
        ( 1, "20" ),
        ( 0, "30" ),
        ( 0, "01" ),
        ( 0, "020" ),
        ( 0, "030" ),
        ( 0, "130" ),
        ( 1, "120" ),
        ( 1, "102" ),
        ( 0, "301" ), 
        ( 2, "12012" ),
        (  96, "213201424147191024" ),
        ( 240, "14221422319194918" ),
        ( 160, "169201418147162113" ),
        (  64, "24191018161781668" ),
        ( 320, "161822127724181318" ),
        (   8, "6281558142375" ),
        ( 320, "171225515182317246" ),
        (  20, "12231452028137" ),
        ( 160, "19241123241817964" ),
        (  80, "316182421239722" ),
        (  96, "14832151725142320" ),
        ( 320, "18917182421161814" ),
        (  64, "141410182510913722" ),
        (  16, "79643158161819" ),
        ( 384, "1522325191923102522" ),
        ( 200, "255122361911161019" ),
        ( 780, "221115141422248225" ),
        (  64, "104241813141420822" ),
        ( 120, "1821513165412197" ),
        ( 160, "109192519151792122" ),
        (  30, "2037194125202213" ),
        (  30, "2037194125202213" ),
        (  20, "20371941025202213" ),
        (  16, "91741914201320110" ),
        (   0, "091741914201320110" ),
        ( 320, "111375142324151323" ),
        (   0, "1113751423024151323" ),
        ( 120, "17124131024381218" ),
        (   0, "171241310240381218" ),
        (  90, "2241213157118205" ),
        (  36, "22412103157118205" ),
        ( 440, "211222117725251014" ),
        (   0, "2112221177250251014" ),
        (  10, "71210201022172720" ),
        (   5, "712010201022172720" ),
        (  72, "4152417116720113" ),
        (  36, "41520417116720113" ),
        ( 104, "1421212220167616" ),
        (   0, "14212122201670616" ),
        (  40, "162521167203153" ),
        (   0, "1602521167203153" ),
    )
    

    for a,b in test_examples:
        assert a == f(b), '( %d, "%s" ) test failed'%(a,b)

    assert 109628489303162558733863437409983623605144821757007311532985475924656536944640000000000000000000000000000 == f("1111013722141511147133422716173231721211585151386131425141471523519572525621096852222131215320189229129239171624192519211914113209211124231151518224211718121112012205223410101691213211214142111762214174115141425211532413222225510173151613241516221972222421209113166922129221414122321823102412322154324142195617162217121681721923242418121611711015171824108119152172101820158182519171719132216101716211324282311222031611217204241421414151651711224623318417752319201681316351791839144231225624161314219121410325219151233201319124118521417181710131722662213252325191517211522225222117192431082410251112616491175271724182412111852110410822419171521812282161015141916817241118918156195241356313122324827818119223139101237165392124918202483211619191829194159191210215169101913222221810962471361312717201719525224291916171462414611579112525")
    assert   0 == f("11110137221415111471334227161732317212115851513861314251414715235195725256210968522221312153201892291292391716241925192119141132092111242311515180224211718121112012205223410101691213211214142111762214174115141425211532413222225510173151613241516221972222421209113166922129221414122321823102412322154324142195617162217121681721923242418121611711015171824108119152172101820158182519171719132216101716211324282311222031611217204241421414151651711224623318417752319201681316351791839144231225624161314219121410325219151233201319124118521417181710131722662213252325191517211522225222117192431082410251112616491175271724182412111852110410822419171521812282161015141916817241118918156195241356313122324827818119223139101237165392124918202483211619191829194159191210215169101913222221810962471361312717201719525224291916171462414611579112525")


def test(S):
    s = S()
    f = lambda x: s.numDecodings(x)
    bundle(f)
    print "test \033[1m%s\033[0m passed"%S.__name__
    #gen_test(f)


if __name__ == "__main__":
    test(SolutionHoriSun)
    test(SolutionXLZ)
    #test(SolutionCong) # not pass
    test(SolutionCong2) 
