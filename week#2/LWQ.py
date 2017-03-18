global array
global num
def recursion(n,n_first):
	
	global num
	num = num + 1
	if (num > len(array)):
		return False
	n_input = (n + array[n])%len(array)
	if(n_input == n):
		return False
	elif(n == n_first):
		return True
	elif(array[n_input]*array[n]>0):
		recursion(n_input,n_first)
	else:
		return False


def aaa(n,na):
	if (n == na):

		return True

if __name__ == "__main__":
        array = input('input an array:')
	global num
	for i in range(len(array)):	
		num = 0;
		loop = recursion(i,i)
		if(loop):
			print 'true'
			break
