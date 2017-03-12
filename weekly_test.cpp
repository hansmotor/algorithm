#include <stdio.h>
#include <math.h>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

#define MAX_AMOUNT 100

int makeChange(int amount, vector<int> &denoms);
int makeChange(int amount, vector<int> denoms, int idx);
bool t_compare(int a, int b);

void main()
{
	cout<<"Give the total amount and different denomination of coins."<<endl;
	cout<<"please enter the amount, using enter to input:";
	int amount;
	cin>>amount;
	if (amount > MAX_AMOUNT)
	{
		cout<<"Exceed the max amount, please enter again:";
		cin>>amount;
	}
	cout<<"please give the number of the coin denomination:";
	int deno_num;
	cin>>deno_num;
	cout<<"please enter the coins:";
	vector<int> coins;
	int x;
	for (int i=0; i<deno_num; i++)
	{
		cin>>x;
		coins.push_back(x);
	}
	int combine_count = makeChange(amount, coins);
	printf("There are %d ways to make up the amount.\n", combine_count);
	char a;
	cin>>a;
}

int makeChange(int amount, vector<int> &denoms) 
{
	int i = makeChange(amount, denoms, 0);
	return i;
}

int makeChange(int amount, vector<int> denoms, int idx)
{
	if (idx >= denoms.size() - 1) 
		return 1;
	int n = denoms.size();
	int *number;
	number = (int *)malloc(n * sizeof(int));
	for (int i = 0; i < n; i++)
	{
		number[i] = denoms[i];
	}
	sort(number,number + n, t_compare);  //降序
	int val = number[idx], res = 0;
	for (int i = 0; i * val <= amount; i++)
	{
		int rem = amount - i * val;
		res += makeChange(rem, denoms, idx + 1);
	}
	return res;
}

bool t_compare(int a, int b)
{
	return a > b;
}
