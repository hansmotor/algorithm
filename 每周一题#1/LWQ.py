global coins
num_of_coms =0
def coinrecursion(n,amount_run):
        if((len(coins)-n) == 1 or amount_run==0):
                if(amount_run % coins[-1] ==0):
                        global num_of_coms
                        num_of_coms  =  num_of_coms+1
        elif((len(coins)-n) >1):
                num =1+ amount_run/coins[n]
                num = min(num,501)
                for i in range(num):
                        #print ("i",i)  
                        coinrecursion(n+1,amount_run-i*coins[n])



def coindp(coins,amount):
	num_of_coms = [0] * (amount+1)
	num_of_coms[0] = 1
	num = [[0 for x in range(amount+1)] for y in range(len(coins))]
	for i in range (len(coins)):
		for j in range (amount-coins[i]+1):
			d_i = j + coins[i]
			if (num[i][j]<500):
				num[i][d_i] = 1+num[i][j]
				num_of_coms[d_i] += num_of_coms[j]
	print 'number of combination:',num_of_coms[-1]


if __name__ == "__main__":
	coins = input('coins(input an array):')
	amount = input('amount:')
	if (max(coins)>5000 or amount > 5000):
		print 'error:the coin or amount is bigger than 5000'
	else:
		coindp(coins,amount)
		#coinrecursion(0,amount)		
		#print 'number of combination:',num_of_coms
