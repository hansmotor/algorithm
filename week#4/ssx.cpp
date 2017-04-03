#include "stdafx.h"
#include <stdio.h>
#include <cstdlib>  
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

//week4-------------------
class NumberInclusiveFind 
{
public:
	vector<int> findInclusiveNumbers(vector<int>& nums) 
	{
		//sort( nums.begin(),nums.end());//ÉýÐòÅÅÐò
		int m_size=nums.size();
		vector<int> temp;
		for(int i=0;i<m_size;i++)
			temp.push_back(0);
		for(int i=0;i<m_size;i++)
		{
			int m=nums[i]-1;
			temp[m]=1;
		}
		vector<int> res;
		for(int i=0;i<m_size;i++)
		{
			if(temp[i]==0)
				res.push_back(i+1);
		}
		return res;
	}
};
int _tmain(int argc, _TCHAR* argv[])
{
	vector<int>mResult;
	vector<int>mInput;
	mInput.push_back(1);
	mInput.push_back(1);
	mInput.push_back(2);
	mInput.push_back(5);
	mInput.push_back(8);
	mInput.push_back(3);
	mInput.push_back(3);
	mInput.push_back(4);
	mInput.push_back(4);
	NumberInclusiveFind m_findnum;
	mResult =m_findnum.findInclusiveNumbers(mInput) ;
	printf("-----------------------------\r\n");
	vector<int>::iterator it;
	for(it=mResult.begin();it!=mResult.end();it++)
		printf("ÔªËØ£º%d\r\n",*it);
	printf("-----------------------------\r\n");

	return 0;
}

