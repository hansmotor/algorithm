// weeks.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <stdio.h>
#include <cstdlib>  
#include <vector>
using namespace std;

vector<int> m_array;
int move(int pos) 
{
	return (pos+m_array.at(pos)+m_array.size()) % m_array.size();
}
bool circularArrayLoop(vector<int>& nums) 
{
	m_array = nums;
	for (int i=0; i<nums.size(); i++) 
	{
		if (nums[i] == 0) 
			continue;
		int j,k;
		j=k=i;
		while (nums[i]*nums[move(k)]>0 && nums[i]*nums[move(move(k))]>0) 
		{
			j = move(j);
			k = move(move(k));
			printf("元素index：%d\r\n",j);
			if (j == k) 
			{
				//检查只有一个元素的环
				if (j == move(j)) 
					break;
				
				return true;
			}
		}
		return false;
	}
}



int _tmain(int argc, _TCHAR* argv[])
{
	//[2, -1, 1, 2, 2]
	vector<int> temp;
	temp.push_back(2);
	temp.push_back(-1);
	temp.push_back(1);
	temp.push_back(2);
	temp.push_back(2);
	printf("\r\n输入[2, -1, 1, 2, 2]\r\n");
	bool mOutput = circularArrayLoop(temp);
	printf("\r\n是否有环：1：有 ； 0：无\r\n结果：%d\r\n",(int)mOutput);
    printf("-----------------------------\r\n");

	return 0;
}

