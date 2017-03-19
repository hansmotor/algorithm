global array
global num
def recursion(n,n_first):	
	global num
	num = num + 1
	n_input = (n + array[n])%len(array)
	if(n_input == n or array[n_input]*array[n]<0):
		return -1
	elif (n_input == n_first or num > len(array) - n_first):
		return -2
	
	else:
		return recursion(n_input,n_first)


def loop(n,n_first):
        global num
        num = num + 1
        n_input = (n + array[n])%len(array)
        if(n_input == n or array[n_input]*array[n]<0):
                return -1
        elif (n_input == n_first or num > len(array)-n_first):
                return -2
        else:
                return n_input


if __name__ == "__main__":
        array = input('input an array:')
	global num
        for i in range(len(array)):                
		isloop = i
		num = 0
		#isloop = recursion(i,i)
		while(isloop >=0):
                	isloop = loop(isloop,i)
		if (isloop == -1 ): continue
		elif (isloop == -2): 
			print 'true'	
			break
        if(isloop == -1):
                print 'false'



