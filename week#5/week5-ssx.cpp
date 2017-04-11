// week5-ssx.cpp : �������̨Ӧ�ó������ڵ㡣
#include "stdafx.h"
#include <stdio.h>
#include <cstdlib>  
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

//a,b,c���������������ֱ�Ϊi,j,k��
//�����򣬴������ͷȷ��һ����a��b��������a��1��cΪ�����β
//a + b + c = 0 ��i++ k-- ��������������¼����
//a + b + c < 0 ��j++
//a + b + c < 0 ��k--��ֹ����b < c��

class Solution 
{
public:
	vector<vector<int>> threeSum(vector<int> &nums) 
	{
		vector<vector<int>> result;
		vector<int> temp;
		sort(nums.begin(), nums.end());

		int n = nums.size();
		for (int i = 0; i < n - 2; ++i) 
		{
			// ȥ�ظ�
			if (i>0 && nums[i-1] == nums[i])
			{
				continue;
			}
			int j = i + 1;
			int k = n - 1;
			while (j < k) 
			{
				if (nums[i] + nums[j] + nums[k] < 0)
				{
					// ȥ�ظ�
					while (j < k && nums[j] == nums[j+1]) 
					{
						j++;
					}
					j++;
				}
				else if (nums[i] + nums[j] + nums[k] > 0)
				{
					// ȥ�ظ�
					while (k > j && nums[k] == nums[k-1]) 
					{
						k--;
					}
					k--;
				}
				else
				{
					temp.push_back(nums[i]);
					temp.push_back(nums[j]);
					temp.push_back(nums[k]);
					result.push_back(temp);
					// ȥ�ظ�
					while (j < k && nums[j] == nums[j+1]) 
					{
						j++;
					}
					while (k > j && nums[k] == nums[k-1]) 
					{
						k--;
					}
					j++;
					k--;
				}
			}
		}
		return result;
	}
};


int _tmain(int argc, _TCHAR* argv[])
{
	vector<vector<int>>mResult;
	vector<int>mInput;
	mInput.push_back(1);
	mInput.push_back(0);
	mInput.push_back(2);
	mInput.push_back(-1);
	mInput.push_back(-2);
	mInput.push_back(-3);
	mInput.push_back(3);
	mInput.push_back(4);
	mInput.push_back(5);
	Solution m_solution;
	mResult =m_solution.threeSum(mInput) ;
	printf("-----------------------------\r\n");
	vector<vector<int>>::iterator iter;
	vector<int>::iterator it;
	static int mBreak =0;
	for(iter=mResult.begin();iter!=mResult.end();iter++)
	{
		
		for (it=iter->begin();it!=iter->end();it++)
		{
			mBreak++;
			printf("Ԫ�أ�%d\r\n",*it); 
			if (mBreak==3)
			{
				printf("-----------------------------\r\n");
				mBreak =0;

			}
		}
	}
		
	printf("-----------------------------\r\n");

	return 0;
}