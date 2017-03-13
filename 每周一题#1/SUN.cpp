#include "stdafx.h"
#include <stdio.h>
#include <cstdlib>  
#include <vector>
using namespace std;

template<typename T,size_t N>  
int LengthofArray(T (&array)[N])
{
	return sizeof(array) / sizeof(T);  
}
int Getway(vector<int>& coins, int amount) 
{
	if (amount == 0) return 0;
	vector<int> dp(amount + 1);
	dp[0] = 1;
	for (int j = 0; j < coins.size(); ++j)
	   for (int i = 1; i < amount + 1; ++i)
		   if(i - coins[j] >= 0)
			   dp[i] = dp[i]+ dp[i - coins[j]] ;

	return  dp[amount];
}

int _tmain(int argc, _TCHAR* argv[])
{
	vector<int> coins;
	coins.push_back(1);
	coins.push_back(2);
	coins.push_back(3);
	coins.push_back(4);
	int target = 7;
	printf("\n   输入1,2,3,4\n\n");
	printf("------amount=7------\n\n");
	int mOutput = Getway( coins,target);
	printf("\r\n打印输出 \"%d\"\r\n",mOutput);
	return 0;
}
